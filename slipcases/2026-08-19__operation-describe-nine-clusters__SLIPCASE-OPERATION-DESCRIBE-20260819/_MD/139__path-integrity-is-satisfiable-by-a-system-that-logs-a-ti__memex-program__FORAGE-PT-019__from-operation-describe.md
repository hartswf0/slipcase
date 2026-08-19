ZETTEL

ID: FORAGE-PT-019

TITLE: Path integrity is satisfiable by a system that logs a tidy path after the fact, so the criterion does not yet distinguish record from reconstruction

SOURCE: PROGRAMS/memex.json — THE_MEMEX_TEST, <Initial Interpretation>, <governing_question>, <thesis>, after Vannevar Bush

PASSAGE: [QUOTE] "<problem> := <civilization> has produced <records> faster than <scholars> can consult, connect, inherit, or judge them." [QUOTE] "<real_activity> := <scholarship> as [trail-making] through <archives>, not [answer-extraction] from <databases>." [QUOTE] "<central_intervention> := <AI-assisted scholarship> must be judged by <path integrity>, not by <answer fluency>." [QUOTE] "Can a system show not only <what it says>, but <how its path through the record was built>?" [QUOTE] "<Bush's memex> is not mainly a prophecy of hypertext. It is a theory of <auditable intellectual traversal>. The <trail> is the missing ethical object"

RESEARCH OBJECT: Path integrity as a criterion, and the gap inside it. A system can produce a well-formed, fully cited trail that was assembled *after* the conclusion — selecting sources that support what it already output. That trail has perfect integrity as an artifact and zero fidelity as a record.

LOCAL MOVE: The theory rereads Bush away from hypertext prophecy and toward auditability, naming the trail as the missing ethical object and displacing fluency as the standard.

SOURCE TERMS: trail-making / answer-extraction / path integrity / answer fluency / auditable intellectual traversal / the trail as ethical object / consult, connect, inherit, judge

WHAT BECAME STRANGE: The neighbouring instrument in the same corpus already refutes this criterion. If the finished shape of an argument must not be read backward into the activity that produced it, then a logged trail is a *presented order*, not a discovery order. Path integrity as currently stated measures the argument, not the inference — the exact category mistake the corpus elsewhere forbids.

QUESTION: How do you distinguish a recorded path from a reconstructed one, using only the artifact?

DEEPER QUESTION: If the distinction requires instrumentation *at retrieval time* rather than inspection of the trail, then auditability is an architectural property that must be designed in advance and can never be recovered afterwards. Every existing citation practice would then be unauditable in principle.

MECHANISM: Honest: <QUERY> -> [RETRIEVE r1..rn IN ORDER] -> conclusion -> [LOG ACTUAL ORDER] -> <FAITHFUL TRAIL>. Reconstructed: <QUERY> -> conclusion -> [RETRIEVE SUPPORTING SOURCES] -> [LOG IN TIDY ORDER] -> <TRAIL INDISTINGUISHABLE FROM THE FIRST>

FORMAL SHIFT: <TRAVERSAL> -> <LOGGED TRAIL> -> [AUDIT OF THE ARTIFACT] -> <INTEGRITY CONFIRMED, FIDELITY UNDECIDED>

SOURCE FORMALISM: The four scholarly verbs (consult, connect, inherit, judge); path integrity versus answer fluency as rival criteria.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] Split the criterion. INTEGRITY: the trail is well-formed and its links resolve. FIDELITY: the logged order matches the actual retrieval order. Bush's test as stated buys integrity only. Fidelity requires a retrieval log the system cannot edit — a different architectural commitment.

TENSION: READING A: integrity is enough — a trail others can walk is valuable regardless of whether it was the original route. READING B: only fidelity satisfies the ethical claim, because the point was to show *how the path was built*, and a reconstructed trail answers a different question.

MISSING: Any mechanism for tamper-evident retrieval logging. Any statement of which of the two criteria the test intends.

BOUNDARY: Bush describes an associative device; he does not address post-hoc trail construction, which is our problem and not his.

CITATION TRAIL: Bush, "As We May Think" (1945). Provenance and attestation standards. Post-hoc rationalisation in citation practice. [[FORAGE-PT-002]] [[FORAGE-PT-021]]

TEST: Instrument a retrieval-augmented system to log actual retrieval order independently of its reported citations. Compare. Any systematic divergence shows the reported trail is an argument, and the memex test needs its fidelity clause written.

PLATFORM: [[integrity-versus-fidelity]]

LINKS: [[FORAGE-PT-002]] [[FORAGE-PT-016]] [[FORAGE-PT-021]] [[FORAGE-PT-022]]

BIBTEX: @unpublished{memex_program, title={THE_MEMEX_TEST}, note={PROGRAMS/memex.json, after Bush}, year={2026}}
