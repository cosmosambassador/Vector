# BEW: Bengali and Punjabi meet medical and technical words

Human authority: TJ Morris. RRRR working revision, 24 October 2026.

BEW is the Basic English Words anchor. Bengali and Punjabi make the meaning available beyond English. This is a small glossary, not a complete medical dictionary or an approved patient translator.

**All Bengali and Punjabi text below is an unreviewed machine draft.** The source resources listed later support review; they do not validate these translations. Punjabi is a language; Punjab is a region. We record Punjabi in Gurmukhi here. Shahmukhi is a separate script path with null labels until reviewed.

| English anchor | Bengali draft | Punjabi, Gurmukhi draft |
| --- | --- | --- |
| care | যত্ন | ਦੇਖਭਾਲ |
| medical care | চিকিৎসাসেবা | ਡਾਕਟਰੀ ਦੇਖਭਾਲ |
| medicine — drug | ওষুধ | ਦਵਾਈ |
| evidence | প্রমাণ | ਸਬੂਤ |
| symptom | উপসর্গ | ਲੱਛਣ |
| signal | সংকেত | ਸੰਕੇਤ |
| measurement | পরিমাপ | ਮਾਪ |
| consent | সম্মতি | ਸਹਿਮਤੀ |
| integrative medicine | সমন্বিত চিকিৎসা | ਏਕੀਕ੍ਰਿਤ ਚਿਕਿਤਸਾ |

## Foundation in the requested languages

- English: **Basic Instruction Before Leaving Earth**.
- Bengali draft: **পৃথিবী ছাড়ার আগে মৌলিক নির্দেশনা**.
- Punjabi draft, Gurmukhi: **ਧਰਤੀ ਛੱਡਣ ਤੋਂ ਪਹਿਲਾਂ ਮੁੱਢਲੀਆਂ ਹਦਾਇਤਾਂ**.

BIBLE remains the English mnemonic. The translated phrase does not recreate the English acronym. TJ's spiritual foundation stays separate from clinical instructions and evidence about treatments.

## East meets West: the meaning bridge

Keep the care tradition, intended use and supporting evidence explicit. A word shared across traditions does not establish that practices have the same mechanism, benefits or risks. A radio signal is not a symptom. A symptom is not a diagnosis. A technical measurement needs a method, units and context. The drug sense of “medicine” stays separate from “medical care.”

WHO describes integrative medicine in terms of an interdisciplinary, evidence-based combination of biomedical and traditional/complementary knowledge and practices. This glossary supplies no treatment, dose or claim that any specific intervention works.

## Run locally

From trivector_basic, Python 3.10+:

```sh
python -m mc6_grimoire.medical_words consent bn
python -m mc6_grimoire.medical_words signal pa-Guru
python -m mc6_grimoire.medical_words signal pa-Arab
```

Expect draft Bengali/Punjabi labels and an unverified null Shahmukhi label. English definitions are project explanations. This command makes no model call and reads no patient data.

## Source and review record

- WHO conceptual reference: https://www.who.int/Health-Topics/Traditional-Complementary-and-Integrative-Medicine
- NHS Inform Bengali resources: https://www.nhsinform.scot/translations/languages/bengali
- NHS Inform Punjabi resources: https://www.nhsinform.scot/translations/languages/punjabi
- UK health interpreting guidance: https://www.gov.uk/guidance/language-interpretation-migrant-health-guide

Resources checked 24 October 2026. We have not copied their translated leaflets. Before patient-facing use, a qualified translator and relevant health reviewer must check the exact term, context, register and intended audience. Reviewers should record their name, date, source and changes. Code tests verify record handling, not medical translation accuracy.

YAML master: records/medical_technical_dictionary.yaml. Packaged JSON: mc6_grimoire/medical_terms.json. Prepared Hugging Face copy: medical_technical_dictionary.yaml. No Hugging Face upload or medical translation service is active.
