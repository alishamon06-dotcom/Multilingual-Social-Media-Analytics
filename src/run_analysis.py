from pathlib import Path
import sys
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, f1_score
from scipy.stats import chi2_contingency
sys.path.insert(0, str(Path(__file__).parent))
from preprocessing import detect_language, normalize_text
from sentiment import lexicon_sentiment, theme_tags

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data/social_posts_synthetic.csv")
df["clean_text"] = df["text"].map(normalize_text)
df["language_pred"] = df["text"].map(detect_language)
df["sentiment_lexicon"] = df["text"].map(lexicon_sentiment)
df["themes"] = df["text"].map(lambda x: ", ".join(theme_tags(x)))

# Gold labels in this generated demonstration dataset are synthetic template labels.
# The 200-row evaluation file must be reviewed/corrected by a human before formal claims.
ev = pd.read_csv(ROOT / "data/evaluation_sample_200.csv")
ev["language_pred"] = ev["text"].map(detect_language)
ev["sentiment_pred"] = ev["text"].map(lexicon_sentiment)
print("Language accuracy:", round(accuracy_score(ev.language_gold, ev.language_pred), 3))
print("Sentiment macro F1:", round(f1_score(ev.sentiment_gold, ev.sentiment_pred, average="macro"), 3))
print("\\nLanguage report\\n", classification_report(ev.language_gold, ev.language_pred, zero_division=0))
print("\\nSentiment report\\n", classification_report(ev.sentiment_gold, ev.sentiment_pred, zero_division=0))

# Save the requested comparison outputs.
language_table = df.groupby("language_gold").agg(posts=("post_id","count")).reset_index()
language_table.to_csv(ROOT/"outputs/language_wise_post_counts.csv",index=False)
theme_table = df.explode("themes") if "themes" in df else df
df["themes"] = df["text"].map(lambda x: ", ".join(theme_tags(x)))
theme_rows=[]
for _, row in df.iterrows():
    for theme in theme_tags(row["text"]):
        theme_rows.append({"language":row["language_gold"],"sentiment":row["sentiment_gold"],"theme":theme})
pd.DataFrame(theme_rows).groupby(["language","sentiment","theme"]).size().rename("posts").reset_index().to_csv(ROOT/"outputs/theme_summary.csv",index=False)
df[["post_id","language_gold","sentiment_gold","sentiment_lexicon","themes"]].to_csv(ROOT/"outputs/annotated_posts.csv",index=False)
print("\\nOutputs written to outputs/.")
