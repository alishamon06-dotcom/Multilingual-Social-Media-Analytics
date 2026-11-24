from collections import Counter
import re
from preprocessing import normalize_text, tokenize

LEXICON = {
 "positive": {"amazing","superb","great","happy","smooth","fast","good","mast","zabardast","nice","paisa","vasool","शानदार","अच्छा","अच्छी","बेहतरीन","तेज","साफ"},
 "negative": {"poor","disappointed","drains","drain","heats","hang","freezes","bad","bakwas","खराब","नहीं","गर्म","अटक","बेकार"},
}
NEGATIONS = {"not","no","nahi","nai","नहीं","mat"}

def lexicon_sentiment(text):
    tokens = tokenize(text)
    score = 0
    for i, token in enumerate(tokens):
        if token in LEXICON["positive"]:
            score += -1 if any(t in NEGATIONS for t in tokens[max(0,i-2):i]) else 1
        elif token in LEXICON["negative"]:
            score += 1 if any(t in NEGATIONS for t in tokens[max(0,i-2):i]) else -1
    if score > 0: return "positive"
    if score < 0: return "negative"
    return "neutral"

def theme_tags(text):
    t = normalize_text(text).lower()
    groups = {
      "Battery": ["battery","बैटरी","backup","drain"],
      "Camera": ["camera","कैमरा","photo","फोटो"],
      "Performance": ["performance","smooth","fast","तेज","hang","अटक"],
      "Display": ["display","screen","डिस्प्ले","स्क्रीन"],
      "Price & value": ["price","कीमत","पैसा","worth","value"],
      "Availability & support": ["launch","launched","available","service","सर्विस","लॉन्च"]
    }
    return [name for name, terms in groups.items() if any(term in t for term in terms)] or ["Other"]
