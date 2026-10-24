# SPDX-License-Identifier: LGPL-2.1-only
"""Offline BEW term lookup. Translation drafts, not clinical guidance."""
import argparse
import json
from importlib.resources import files

def load_record():
    return json.loads(files("mc6_grimoire").joinpath("medical_terms.json").read_text(encoding="utf-8"))

def lookup(term, language):
    record = load_record()
    if term not in record["terms"] or language not in record["language_variants"]:
        raise ValueError("Unknown term or language/script tag")
    entry = record["terms"][term]
    return {"concept":term,"language":language,"script":record["language_variants"][language],
            "definition_en":entry["definition_en"],**entry["labels"][language],"review":record["review"]}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("term", choices=sorted(load_record()["terms"]))
    p.add_argument("language", choices=sorted(load_record()["language_variants"]))
    args = p.parse_args()
    print(json.dumps(lookup(args.term,args.language),ensure_ascii=False,indent=2))

if __name__ == "__main__": main()
