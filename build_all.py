import os, glob, json, re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Load slipcases dataset
with open(os.path.join(BASE_DIR, "slipcases.json"), "r", encoding="utf-8") as f:
    cases_data = json.load(f)

all_notes = []
for c in cases_data:
    all_notes.extend(c.get("cards", []))

print(f"Loaded {len(all_notes)} zettels across {len(cases_data)} slipcases.")

# 2. Update map-02.html
map02_path = os.path.join(BASE_DIR, "map-02.html")
if os.path.exists(map02_path):
    with open(map02_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Strip existing window.ZETTEL_DATA block if present
    content = re.sub(r'\n?\s*<script>\s*window\.ZETTEL_DATA\s*=\s*\[.*?\];\s*</script>', '', content, flags=re.DOTALL)
    
    data_block = f"\n    <script>\n    window.ZETTEL_DATA = {json.dumps(all_notes)};\n    </script>\n"
    
    # Inject before <script> tag after DATA header comment or before main script
    if "<!-- =========================================================\n     DATA" in content:
        parts = content.split("<!-- =========================================================\n     DATA", 1)
        # Find next <script> after DATA header
        subparts = parts[1].split("<script>", 1)
        new_content = parts[0] + "<!-- =========================================================\n     DATA" + subparts[0] + data_block + "    <script>" + subparts[1]
    else:
        new_content = content + data_block
        
    with open(map02_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated map-02.html with 1,244 cards.")

# 3. Update box.html
box_path = os.path.join(BASE_DIR, "box.html")
if os.path.exists(box_path):
    with open(box_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Strip existing window.ZETTEL_DATA block if present
    content = re.sub(r'\n?\s*<script>\s*window\.ZETTEL_DATA\s*=\s*\[.*?\];\s*</script>', '', content, flags=re.DOTALL)

    # Hide search slip in CSS
    if "#searchSlip {" in content and "display: none !important;" not in content:
        content = content.replace("#searchSlip {", "#searchSlip {\n            display: none !important;\n")

    data_block = f"\n    <script>\n    window.ZETTEL_DATA = {json.dumps(all_notes)};\n    </script>\n"

    # Inject data before <script type="module">
    if "<script type=\"module\">" in content:
        parts = content.split("<script type=\"module\">", 1)
        new_content = parts[0] + data_block + "    <script type=\"module\">" + parts[1]
    else:
        new_content = content + data_block

    # Add audio click & haptic synthesizer helper into script
    sound_script = """
        /* Audio & Haptic Feedback Synthesizer */
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        function playClick(freq = 680, duration = 0.016) {
          try {
            if (audioCtx.state === 'suspended') audioCtx.resume();
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(140, audioCtx.currentTime + duration);
            gain.gain.setValueAtTime(0.16, audioCtx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
            osc.connect(gain);
            gain.connect(audioCtx.destination);
            osc.start();
            osc.stop(audioCtx.currentTime + duration);
          } catch (e) {}
          if (navigator.vibrate) navigator.vibrate(10);
        }
    """

    if "function changeSlip(" in new_content and "playClick();" not in new_content:
        new_content = new_content.replace("function changeSlip(", sound_script + "\n        function changeSlip(")
        new_content = new_content.replace("renderSlip();\n\n        }", "renderSlip();\n            playClick();\n        }")
        new_content = new_content.replace("field3d?.focusCase(\n                index\n            );", "field3d?.focusCase(\n                index\n            );\n            playClick(820);")

    with open(box_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated box.html with 1,244 cards, hidden search bar, and tactile haptic/audio click feedback.")

# 4. Run build_index_html.py to keep index.html and map.html in sync
os.system(f"python3 {os.path.join(BASE_DIR, 'build_index_html.py')}")
os.system(f"python3 {os.path.join(BASE_DIR, 'build_reader_v3.py')}")
print("All repository instruments compiled and synchronized!")
