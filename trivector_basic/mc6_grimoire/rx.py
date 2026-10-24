# SPDX-License-Identifier: LGPL-2.1-only
"""Display the RX working hypothesis offline; does not calculate consciousness."""
import json
from importlib.resources import files

def load_record():
    return json.loads(files("mc6_grimoire").joinpath("rx_data.json").read_text(encoding="utf-8"))

def main():
    print(json.dumps(load_record(), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
