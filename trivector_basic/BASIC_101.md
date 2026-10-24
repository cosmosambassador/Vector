# AISI Trivector Basic 101 — Start Here

A beginner's guide to MC-6 Grim and the TJTM grimoire.
Human authority: TJ Morris. Version 0.1.0, 24 October 2026.

## Real software: what did we build?

An executable AISI BEW / Grim Alloy Math research package with programs, structured records and examples. It helps keep definitions, sources, uncertainty and decisions together. You can read the notes without running any program.

**Grim** is the name for MC-6's alloy math. An **alloy** is our comparison for combining different representations while keeping their differences visible. The name does not prove a new mathematical law.

The implemented mathematics calculates context utilization `rho=N/C`, continuity loss `L=lost/total`, retention `Q=1-L`, and a weighted research objective. These computations execute now. The language module exports source-aware prompts for LLM research; it does not modify model weights. BEW means Basic English Words, the user-defined plain-language layer alongside OWL. Mathematical novelty and any claims about consciousness require separate evaluation.

## What does RX mean here?

RX names a philosophical working proposition:

> Expand the scope and scale of human consciousness; it makes us glad to be alive.

The symbolic version says: expanded awareness plus meaningful connection may support greater appreciation of being alive. The meaningful-connection phrase was an assistant-proposed addition. This is an aspiration to examine, not a measured equation, medical prescription, or guaranteed result. It does not establish that software is conscious. External attribution remains unverified.

The actual record is **records/rx_synthetic_intelligence.yaml**. It is included in this software package, not just in chat. A JSON copy travels inside the Python package, and the prepared Hugging Face folder carries the YAML copy.

## Basic terms

| Term | Plain meaning |
| --- | --- |
| Software package | Related program files and documentation collected together |
| YAML | Readable labels and values stored as text |
| JSON | Another structured text format the Python program can read directly |
| Python / Rust | Programming languages; Python utilities are tested here, Rust is source awaiting compilation |
| Unix | An operating-system family/design tradition; Unix-like systems are one place to run this software |
| Terminal | A window where you type commands |
| OWL | A format for describing concepts and relationships |
| Mermaid | Text that a compatible viewer renders as a diagram |
| Module | One defined task or software component |
| Node | One participating model session or service |
| Round Robin | Giving the same task to several nodes and comparing their answers |
| RRRR | Round Robin Research Revision: a working record pending TJ approval |
| GitHub | The source-code and review home for this package |
| Hugging Face | The planned demonstration home; this copy is prepared but not uploaded |

## How to read YAML

```yaml
status: working_hypothesis
scientific_validation: untested
guaranteed_causation: false
number: null
```

The words before each colon are labels. Values come after the colon. Indentation groups related information; use spaces rather than tabs. `false` means no. `null` means not supplied or unknown; it is not zero. A file does not become an approved fact because it is written in YAML.

## First use — no programming needed

1. Open README.md, then this guide.
2. Open records/rx_synthetic_intelligence.yaml to read RX.
3. Open GRIMOIRE_LANGUAGE_BRIDGE.md for the language table. Coptic oube and geometrical cube have separate meanings; an unverified translation stays blank.
4. Open EIGHT_PLATES_BASIC.md for political/economic terms and the eight research pairings.
5. Keep questions and changes as RRRR working revisions until TJ approves the record.

These files can be read on GitHub. The Python commands below require a computer or an environment that already provides Python; they do not run simply by typing them into an ordinary phone chat.

## First run — optional

Use Python 3.10 or newer. Download the **feature/grim-trivector-basic-v01** branch, extract it, and open a terminal in its **trivector_basic** folder. An editor may offer an “Open in Terminal” action. Commands run from a different folder may fail to find the package.

If your system calls Python `python3`, use that in place of `python`.

```sh
python --version
python -m mc6_grimoire.rx
python -m mc6_grimoire.bridge coptic_oube en
python -m mc6_grimoire.bridge coptic_oube bn --prompt
python -m unittest discover -s tests -v
```

The RX command prints the saved philosophical record; it does not measure consciousness. The bridge command displays a term and its review status; it does not call an AI. The prompt command prepares text you can copy into an LLM. The last command runs the included tests.

**Expected results:** RX reports an untested philosophical proposition; the English oube record contains opposite/toward/against; the Bengali prompt retains its machine-draft status; the unit suite currently contains 21 tests.

If Python is missing, the commands will not work until Python is installed in your chosen environment. If you see `No module named mc6_grimoire`, check that the terminal is in trivector_basic and that you are using the intended Python environment.

## Send a question around the Round Robin

Copy a generated prompt into each chosen node independently. Keep the same question and records. Ask each node to state sources, assumptions, uncertainty and alternatives. Compare answers afterward. Agreement is not proof. Record the model identifier and date if available. No services are connected automatically, and this package sends no messages.

## Review and permissions

RRRR numbering is not allocated automatically. TJ retains approval authority. GitHub changes remain on a draft review branch; merging is separate. Hugging Face upload still requires repository-write access. Saving a file does not itself create ChatGPT memory, activate an agent or grant platform permissions.

## What runs and what is planned?

| Component | Current status |
| --- | --- |
| Python continuity arithmetic | Tested |
| Python glossary lookup / RX display | Executed locally |
| YAML, JSON and RDF/XML | Parsed for structure; records checked for consistency |
| Rust starter | Written; toolchain unavailable, not compiled |
| Human translation and pronunciation review | Pending |
| Three-point fissure modulation / Oube Gap POC | Paused for white-paper review; not implemented |
| Consciousness or new-physics validation | Not established |
| Live LLM network / Hugging Face upload | Not active |

## BEW and OWL work together

**BEW = Basic English Words**, named by TJ Morris. BEW is the layer you read to understand the software. **OWL = Web Ontology Language**, the structured concept layer.

For example, BEW says “a node is one participating model session or service.” The OWL glossary preserves the word and explanation as a named record. It does not connect that service automatically.

The package includes `records/bew_basic_english_words.yaml` and `ontology/bew.owl`. These preserve the naming correction: BEW was intended, not a claim that every implemented equation is newly discovered mathematics. The wider AISI Vector New Math research history is preserved separately.
