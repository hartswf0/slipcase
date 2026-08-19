ZETTEL

ID: FORAGE-PT-016

TITLE: The practice theory ranks four things and demotes every transferable one, which makes it anti-documentation by construction

SOURCE: PROGRAMS/theory.json — NAUR_EHN_MUSASHI_SOFTWARE_PRACTICE_ENGINE, <core_claim>

PASSAGE: [QUOTE] "<software_development> is not <artifact_production>. <software_development> is <shared_theory_building_under_change>. <program_text> is a residue. <documentation> is a residue. <method> is a tool. <AI_code> is a candidate artifact. <program_theory> is the living possession that lets <team> [explain], [justify], [modify], [teach" [QUOTE] "<Peter_Naur> [teaches] <programming_as_theory_building> <Pelle_Ehn> [teaches] <design_as_participatory_language_game> <Miyamoto_Musashi> [teaches] <tool_pluralism_reflective_practice_and_victory_without_waste>"

RESEARCH OBJECT: A four-tier ranking — living possession > tool > residue > candidate artifact — in which everything that can be handed to another person is demoted, and the one thing that cannot be handed over is elevated. The theory is therefore structurally hostile to its own written form.

LOCAL MOVE: It splits the artifact from the capacity and puts all the value in the capacity, with three lineages converging on the same demotion.

SOURCE TERMS: theory building / shared theory / residue / candidate artifact / living possession / explain, justify, modify, teach / participatory language game / victory without waste

WHAT BECAME STRANGE: The four verbs of possession — explain, justify, modify, teach — are not equally hard, and only one of them is diagnostic. Explanation and justification can be produced fluently without possession. **Modification cannot.** So the theory contains its own test and does not name it: the diagnostic is whether someone can change the system without breaking its coherence.

QUESTION: Is there any medium in which a theory transfers, or is transfer always reconstruction in the receiver — and if always reconstruction, what do residues actually do?

DEEPER QUESTION: If residues only *trigger* reconstruction rather than carry theory, then documentation quality should be measured by how reliably it triggers correct reconstruction, not by completeness. That is a different design goal and it would change how everyone writes docs.

MECHANISM: <TEAM HOLDS THEORY> -> [WRITES RESIDUES] -> team disperses -> [NEW READER RECONSTRUCTS FROM RESIDUES] -> reconstruction may differ silently -> [DIVERGENCE INVISIBLE UNTIL MODIFICATION] -> <BREAKAGE REVEALS THE GAP>

FORMAL SHIFT: <LIVING THEORY> -> <RESIDUE> -> [RECONSTRUCTION BY A SECOND MIND] -> <SAME OR DIVERGENT THEORY, DETECTABLE ONLY UNDER CHANGE>

SOURCE FORMALISM: The four-tier ranking; the four possession verbs.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Give a competent stranger only the residues and a *modification* task, not a comprehension task. Score whether the original holder judges the modification coherent. Then ablate the residues to find the minimum set that still triggers correct reconstruction.

TENSION: READING A (strong Naur): the test fails; the reader produces plausible changes the holder rejects, because the mapping to the world lives in people. READING B: with enough explicit constraint the mapping externalises far enough for correct modification, and theory transfer is a matter of degree.

MISSING: Any second reader. Any ablation. The theory asserts non-transferability and never tests it — which is the one thing it could test.

BOUNDARY: Naur argues from software maintained over years by teams. Whether a research corpus or a design document is the same kind of object needs its own argument.

CITATION TRAIL: Naur, "Programming as Theory Building" (1985). Ehn on design-by-doing and mockups. Musashi, The Book of Five Rings. [[FORAGE-PT-008]] [[FORAGE-PT-026]] [[FORAGE-PT-027]]

TEST: One stranger, the residues only, one modification task, holder judges coherence blind. A single trial distinguishes "produces nothing usable" from "produces something the holder recognises" — and that is the whole disagreement.

PLATFORM: [[modification-is-the-only-diagnostic]]

LINKS: [[FORAGE-PT-008]] [[FORAGE-PT-019]] [[FORAGE-PT-026]]

BIBTEX: @unpublished{theory_program, title={NAUR_EHN_MUSASHI_SOFTWARE_PRACTICE_ENGINE}, note={PROGRAMS/theory.json}, year={2026}}
