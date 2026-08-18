ZETTEL

ID: INFERENCE-FORAGE-003

TITLE: SOMEONE ELSE CAN SPEND YOUR PRIVACY

SOURCE: Mathias Humbert, Erman Ayday, Jean-Pierre Hubaux, and Amalio Telenti — “Quantifying Interdependent Risks in Genomic Privacy” — ACM Transactions on Privacy and Security 20(1), Article 3, 2017 — https://doi.org/10.1145/3035538

PASSAGE: [PARAPHRASE] The authors formalize reconstruction attacks in which observing one family member’s genome or phenotype enables inference about unobserved relatives by combining familial inheritance, correlations among genomic variants, and genotype–phenotype relationships.

RESEARCH OBJECT: [[INFERENCE-FORAGE-002]] argued abstractly that one person’s disclosure can change what institutions know about another. Genomic privacy provides a brutally concrete implementation. The target need not disclose anything. A relative discloses; correlation supplies the missing bridge; belief propagation reduces uncertainty about the target. Privacy loss is therefore an event that can happen to a person without an action occurring at that person.

LOCAL MOVE: Execute the strongest unresolved edge in [[INFERENCE-FORAGE-002]]: find a system where opting out demonstrably fails because information supplied by related others permits reconstruction of the nonparticipant.

SOURCE TERMS: interdependent privacy; kin genomic privacy; reconstruction attack; graphical models; belief propagation; Mendel’s Laws; linkage disequilibrium; phenotype; genomic privacy metrics; health privacy

WHAT BECAME STRANGE: [OUR INFERENCE] Privacy ceases to look like possession. I can keep every byte of my genome secret and still lose genomic privacy because another person reveals theirs. The protected quantity is not merely “my data.” It is an adversary’s uncertainty about me, and someone else can reduce that uncertainty.

QUESTION: If privacy is partly the uncertainty others retain about a person, who has authority to spend that uncertainty?

DEEPER QUESTION: Does meaningful consent become logically impossible for information whose inferability is jointly determined by the disclosures of many correlated people?

MECHANISM: Relative reveals genome and/or phenotype → attacker encodes familial structure and inheritance relations → correlations among variants and between phenotype and genotype add constraints → graphical inference / belief propagation updates probabilities for hidden genomic values → attacker uncertainty about the nondisclosing relative decreases → previously concealed health-related information can become more predictable.

FORMAL SHIFT: FROM: PRIVACY LOSS REQUIRES TARGET DISCLOSURE. TO: CORRELATED OTHER DISCLOSURE + INFERENCE CAN REDUCE TARGET PRIVACY WITHOUT TARGET PARTICIPATION.

SOURCE FORMALISM: The source models family relationships and genomic dependencies using graphical models and performs reconstruction using belief propagation. It combines Mendelian inheritance, statistical dependencies between variants, and relationships between phenotypes and genomic variants, then quantifies resulting changes in genomic and health privacy.

OUR FORMALIZATION: [OUR FORMALIZATION — NOT SOURCE SYNTAX] SECRET(X) + DISCLOSE(DATA_RELATIVE) + CORRELATION(X,RELATIVE) + INFERENCE → POSTERIOR(X) MORE CERTAIN; ACTION(X)=NONE BUT PRIVACY(X)↓

TENSION: Genomic kinship is unusually strong because biological inheritance provides explicit correlations. The parent’s biometric problem is broader: companies may infer properties from merely similar people who need not be relatives. The genomic case therefore proves interdependent privacy can exist, but it does not establish that every population-level biometric inference has the same structure or strength.

MISSING: A general measure of interdependent inferential privacy that works when relations are learned statistically rather than inherited biologically; a way to quantify how much one participant’s multimodal biometric disclosure alters the inferability of traits about nonparticipants in the same learned cluster.

BOUNDARY: The inference machinery concerns genomic and phenotypic relations within families. Extending the result from kinship to facial, behavioral, physiological, or multimodal biometric similarity requires new empirical evidence rather than analogy alone.

CITATION TRAIL: [[INFERENCE-FORAGE-002]] → relational data theory says one person’s data can affect another → Humbert et al. provide executable reconstruction attacks where relatives’ disclosures reduce a nondiscloser’s genomic privacy → next edge: replace biological kinship edges with machine-learned similarity edges and ask whether an equivalent privacy-loss calculus can be constructed for biometric inference

TEST: Construct paired inference experiments. In the first, reproduce a kin-genomic setting where target data are withheld while relatives’ data are progressively released. In the second, build a biometric dataset where target participants are withheld but increasingly many statistically similar peers contribute multimodal features. For each release step calculate the reduction in uncertainty about a protected target attribute. Compare the curves. If peer disclosures systematically reduce uncertainty without target participation, then “someone else can spend your privacy” extends beyond kinship into population-level biometric inference.

PLATFORM: GENOMIC PRIVACY / GRAPHICAL MODELS / BELIEF PROPAGATION / INTERDEPENDENT INFERENCE

LINKS: [[INFERENCE-FORAGE-002]]

BIBTEX: @article{humbert2017interdependent, author={Humbert, Mathias and Ayday, Erman and Hubaux, Jean-Pierre and Telenti, Amalio}, title={Quantifying Interdependent Risks in Genomic Privacy}, journal={ACM Transactions on Privacy and Security}, volume={20}, number={1}, articleno={3}, year={2017}, doi={10.1145/3035538}, url={https://doi.org/10.1145/3035538}}
