/**
 * FIGURE CORPS Transcript Agent / Provider Adapter
 * Version 0.8
 *
 * Keeps source acquisition OUT of the LLM system instruction.
 * StoryCorps' current Terms prohibit automated scraping/extraction, so this
 * adapter does not automate DOM clicking/copying from StoryCorps. The
 * authorized provider seam is where an approved research/API route plugs in.
 */

export class FigureCorpsTranscriptAgent {
  constructor({ authorizedBaseURL = "", authorizationToken = "" } = {}) {
    this.authorizedBaseURL = authorizedBaseURL.replace(/\/$/, "");
    this.authorizationToken = authorizationToken;
  }

  sourceURL(record) {
    const id = String(record?.id || record?.["@id"] || record?.url || "");
    if (/^https?:\/\/(www\.)?storycorps\.org\//i.test(id)) {
      return id.replace(/^http:/i, "https:");
    }
    const name = record?.name || record?.title || "StoryCorps";
    return "https://storycorps.org/?s=" + encodeURIComponent(name);
  }

  openSource(record) {
    const url = this.sourceURL(record);
    window.open(url, "_blank", "noopener,noreferrer");
    return {
      state: "awaiting_user_evidence",
      source_url: url,
      next: "Provide transcript text you are authorized to use."
    };
  }

  async ingestText(text, { sourceURL = "", sourceKind = "user-supplied" } = {}) {
    const raw = String(text || "").trim();
    if (!raw) throw new Error("Transcript text is empty.");
    const turns = parseSpeakerTurns(raw);
    if (turns.length < 2) throw new Error("Could not find speaker-labeled transcript turns.");
    return {
      state: "ready",
      source: {
        kind: sourceKind,
        page_url: sourceURL || null,
        raw_sha256: await sha256(raw),
        ingested_at: new Date().toISOString()
      },
      transcript: { turns, sha256: await sha256(JSON.stringify(turns)) }
    };
  }

  async getAuthorized(record) {
    if (!this.authorizedBaseURL) throw new Error("No authorized transcript provider configured.");
    const source = this.sourceURL(record);
    const u = new URL(this.authorizedBaseURL + "/transcript");
    u.searchParams.set("record_url", source);
    const headers = {};
    if (this.authorizationToken) headers.Authorization = "Bearer " + this.authorizationToken;
    const r = await fetch(u, { headers });
    if (!r.ok) throw new Error(`Authorized provider returned HTTP ${r.status}`);
    const data = await r.json();
    if (!data?.transcript) throw new Error("Authorized provider returned no transcript.");
    const ingested = await this.ingestText(data.transcript, {
      sourceURL: data.source_url || source,
      sourceKind: "authorized-provider"
    });
    ingested.source.provider_provenance = data.provenance || null;
    return ingested;
  }
}

export function parseSpeakerTurns(text) {
  const out = [];
  let current = null;
  const lines = String(text).split(/\r?\n/);
  const speaker = /^\s*(?:\[(\d{1,2}:\d{2}(?::\d{2})?)\]\s*)?([^:\n]{1,80}):\s*(.+)\s*$/;
  for (const rawLine of lines) {
    const line = rawLine.trim();
    if (!line) continue;
    const m = line.match(speaker);
    if (m) {
      current = {
        i: out.length + 1,
        speaker: m[2].trim(),
        text: m[3].trim(),
        start: m[1] || null,
        end: null
      };
      out.push(current);
    } else if (current) current.text += " " + line;
  }
  return out;
}

async function sha256(value) {
  const b = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(String(value)));
  return [...new Uint8Array(b)].map(x => x.toString(16).padStart(2, "0")).join("");
}
