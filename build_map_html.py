import os, json, re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Load slipcases dataset
with open(os.path.join(BASE_DIR, "slipcases.json"), "r", encoding="utf-8") as f:
    cases_data = json.load(f)

all_notes = []
for c in cases_data:
    all_notes.extend(c.get("cards", []))

map_path = os.path.join(BASE_DIR, "map.html")
if os.path.exists(map_path):
    with open(map_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Strip existing window.ZETTEL_DATA block if present
    content = re.sub(r'\n?\s*<script>\s*window\.ZETTEL_DATA\s*=\s*\[.*?\];\s*</script>', '', content, flags=re.DOTALL)

    # Replace double-click requirement for opening reader with immediate single click
    old_double_click = """                if (
                    picked.kind === "SLIP"
                ) {

                    const now =
                        performance.now();


                    const isDouble =
                        lastClick.id === picked.id &&
                        now - lastClick.time < 320;


                    lastClick = {
                        id: picked.id,
                        time: now
                    };


                    if (isDouble) {

                        openReader(
                            picked.id
                        );

                    } else {

                        toggleSlipSelection(
                            picked.id
                        );
                    }
                }"""

    new_single_click = """                if (
                    picked.kind === "SLIP"
                ) {
                    openReader(
                        picked.id
                    );
                    if (navigator.vibrate) navigator.vibrate(10);
                }"""

    if old_double_click in content:
        content = content.replace(old_double_click, new_single_click)

    # Re-inject live dataset
    data_block = f"\n    <script>\n    window.ZETTEL_DATA = {json.dumps(all_notes)};\n    </script>\n"

    if "<script type=\"module\">" in content:
        parts = content.split("<script type=\"module\">", 1)
        new_content = parts[0] + data_block + "    <script type=\"module\">" + parts[1]
    else:
        new_content = content + data_block

    with open(map_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Updated map.html: single-click opens reader immediately for all {len(all_notes)} cards.")
