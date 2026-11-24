# Multilingual Social Media Analytics

A small Python project exploring how people discuss a fictional smartphone launch in English, Hindi and Hinglish. I built this as a reproducible NLP workflow, with an emphasis on the messy text that appears in social posts: mixed scripts, spelling variations, emojis and hashtags.

## What is included
- 3,000 reproducible synthetic posts (`data/social_posts_synthetic.csv`)
- A 200-post evaluation sample (`data/evaluation_sample_200.csv`)
- Unicode normalisation, emoji labels, hashtag handling and transliteration-aware tokenisation
- A baseline language detector and a custom Hinglish-aware sentiment lexicon
- Theme tagging and language-wise output tables
- A notebook to explore the workflow and a script that writes CSV outputs

## Dataset note
The dataset is **synthetic**, not scraped from real users or a real brand. The gold labels are generated from controlled templates so the workflow can be tested without collecting personal data. The 200-row file is an evaluation *starter set*: please manually review and correct its language and sentiment labels before reporting the scores as human-annotated evaluation results. Synthetic-template scores should not be presented as real-world model performance.

## Run it
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python src/run_analysis.py
jupyter notebook notebooks/analysis.ipynb
```

The core pipeline uses pandas and scikit-learn. A multilingual transformer comparison is described as an optional extension in the notebook; it requires downloading a model and should be evaluated on the same human-reviewed split.

## Reproducibility
Random seed: `42`. The sample selection and synthetic dataset generation are deterministic.

## Limitations and responsible use
- Hindi written in Roman script can look similar to English; a short post may not contain enough evidence for reliable language detection.
- Sarcasm, regional slang, dialects and context-dependent phrases are difficult for simple lexicons.
- Emoji meanings vary by community and context.
- The sample is balanced by construction and does not represent the actual distribution of Indian social media.
- Do not use language or sentiment labels to make decisions about individual users. Report uncertainty and inspect errors by language group.

## Next steps
1. Have two reviewers independently label the 200-post sample.
2. Resolve disagreements and record an annotation guide.
3. Compare the lexicon baseline with a multilingual transformer (for example, XLM-R) on a fixed stratified split.
4. Report macro F1, per-class results and per-language error rates with confidence intervals.
