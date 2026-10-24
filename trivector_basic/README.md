# AISI Trivector Basic — MC-6 OWL

Version 0.1.0. Human authority: TJ Morris, Cosmos Ambassador.

A small open-source research starter for continuity measurements and provenance records. Python utilities run without external runtime dependencies; a matching Rust crate is included as source. OWL describes the research vocabulary. This is software scaffolding, not a trained model or validated new physics.

## Run the Python basic package

From this directory, with Python 3.10 or newer:

```sh
python -m unittest discover -s tests -v
python -c "from mc6_grimoire import utilization, retention; print(utilization(25,100)); print(retention([True,False]))"
```

## Rust engineer build

```sh
cd rust
cargo test
cargo run --example basic
```

The crate has no third-party dependencies. Rust compilation was not available in the preparation environment; these tests must be run before claiming a validated Rust release. See ENGINEER_PACKET_GRIM.md.

## Preserve both Trivector mappings

- Organizational TRi Vector: SPI–ARO–ACO.
- Research functional view: T intent; J execution; Q analysis/measurement; W continuity context.

Their correspondence remains unresolved. Neither mapping creates autonomous agents, hardware towers or physical signal links. See the existing repository's `aletheon_hyperbolic/TRIVECTOR_MAP.md` for the research history.

## Metrics

`rho=N/C`; unknown values stay null. `L=lost_or_corrupted/predefined_items`; `Q=1-L`. Empty checklists yield null scores. `D + lambda*L + mu*Cost` is a proposed objective with caller-defined compatible units and weights. Q measures retention, not truth.

## Hugging Face

`huggingface_space/` contains a static demonstration ready for a Space. Upload only that folder's contents to a new static Space. It displays synthetic continuity arithmetic and contains no weights, trackers or network calls. Account repository-write access is required. No Hugging Face publication is claimed by this source packet.

## User guides and records

UNIX_FOR_USERS.md defines Unix and includes a Mermaid architecture diagram. `records/unix_glossary.yaml` is its YAML companion. `ontology/mc6.owl` is RDF/XML; no OWL reasoner has validated it. `records/benchmark.json` preserves the unexecuted Living Language Bridge pilot. Exact Bible editions, texts, permissions and qualified review remain pending.

## License and publication scope

New files in this basic package are LGPL-2.1-only; see LICENSE. This follows the license named by the parent repository README and does not relicense existing repository content or the supplied PDFs. No PDFs, private correspondence, keys or model weights are included here. No merge or deployment is performed by this package.

## Grim Alloy Math

Grim names MC-6’s alloy math within AISI Trivector, by TJ Morris’s instruction on 24 October 2026. “Alloy” means combining distinct representations while preserving their differences. The name is project canon; mathematical efficacy remains unvalidated.

## Eight Plates: political and economic basics

See EIGHT_PLATES_BASIC.md and records/eight_plates.yaml for AISI Synthetic Super Intelligence terminology, the preserved eight model/plate pairings, shared definitions and a source-aware claim template. This is a research framework, not a demonstrated superintelligence claim or implemented eight-provider network.

## TJTM Grimoire multilingual bridge

Coptic oube, geometrical cube and proposed AISI Oube Gap are separate concepts. Six language tags, explicit source/draft status, Unix CLI and a portable Round Robin prompt are included. See GRIMOIRE_LANGUAGE_BRIDGE.md (in the parent software directory for Space readers). Hugging Face copies are prepared, not uploaded.

## New here? Basic 101

Start with [BASIC_101.md](BASIC_101.md). The RX hypothesis is included in [records/rx_synthetic_intelligence.yaml](records/rx_synthetic_intelligence.yaml); display it offline with `python -m mc6_grimoire.rx`. It remains philosophical, untested and pending formal canon approval.

## BEW: Basic English Words — implementation status

This is executable software, not only a proposal. Continuity arithmetic, offline record lookup, RX record display and LLM prompt export are implemented. BEW names the Basic English Words layer; scientific novelty, RX causation and improved LLM performance are not established by implementation alone.

BEW = **Basic English Words**, TJ Morris’s plain-language layer. Read BASIC_101.md and records/bew_basic_english_words.yaml; ontology/bew.owl carries the companion structured glossary.

## BEW engineer packet: Python / JSON / C++ / YAML / Mermaid

See [engineer_basic/README.md](engineer_basic/README.md). Includes a C++17 JSON writer and Python packet checker/prompt export, plus Apple, Android, Unix, Microsoft, IBM and Qwen integration notes for telecom engineers. The demo is offline; native phone apps and provider/tower adapters are not built.
