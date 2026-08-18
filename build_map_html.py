import os, json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "slipcases.json"), "r", encoding="utf-8") as f:
    cases = json.load(f)

all_notes = []
for c in cases:
    all_notes.extend(c.get("cards", []))

with open(os.path.join(BASE_DIR, "map.html"), "r", encoding="utf-8") as f:
    map_html = f.read()

# Check if window.ZETTEL_DATA is already injected
if "window.ZETTEL_DATA" in map_html and "/* DATA_NOTES */" not in map_html and "window.ZETTEL_DATA =" in map_html:
    # Replace existing injection or re-inject before <script type="module">
    import re
    map_html = re.sub(r'<script>\s*window\.ZETTEL_DATA\s*=\s*\[.*?\];\s*</script>', '', map_html, flags=re.DOTALL)

data_script = f"\n    <script>\n    window.ZETTEL_DATA = {json.dumps(all_notes)};\n    </script>\n"

# Inject before <script type="module">
if "<script type=\"module\">" in map_html:
    parts = map_html.split("<script type=\"module\">", 1)
    new_map_html = parts[0] + data_script + "    <script type=\"module\">" + parts[1]
else:
    new_map_html = map_html + data_script

with open(os.path.join(BASE_DIR, "map.html"), "w", encoding="utf-8") as f:
    f.write(new_map_html)

print(f"Successfully wired map.html with {len(all_notes)} cards across all {len(cases)} slipcases.")
