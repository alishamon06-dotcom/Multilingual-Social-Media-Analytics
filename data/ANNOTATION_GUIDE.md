# Human annotation guide

Use this guide to review `evaluation_sample_200.csv`. Work from the original post text, not the existing labels.

## Language
- English: primarily English wording.
- Hindi: primarily Devanagari Hindi.
- Hinglish: Hindi grammar/words written mainly in Latin script, often mixed with English.
- If both scripts are materially present, use `Code-mixed` (extend the schema consistently).

## Sentiment
- positive: clear praise or satisfaction.
- negative: clear complaint or dissatisfaction.
- neutral: factual question, announcement or statement without clear polarity.
- Sarcasm or unclear context: mark `uncertain` in a separate notes column and discuss it; do not force certainty.

Have two people label independently if possible, resolve disagreements, and preserve a copy of the original starter file.
