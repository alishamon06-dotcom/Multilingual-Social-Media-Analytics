import re
import unicodedata

EMOJI_MAP = {"😍":" positive_emoji ", "🔥":" positive_emoji ", "😊":" positive_emoji ",
             "❤️":" positive_emoji ", "😡":" negative_emoji ", "😞":" negative_emoji ",
             "👎":" negative_emoji ", "😭":" negative_emoji ", "😂":" laughing_emoji ",
             "🤔":" thinking_emoji ", "📱":" phone_emoji ", "✨":" sparkle_emoji "}

def normalize_text(text):
    text = unicodedata.normalize("NFKC", str(text))
    for emoji, label in EMOJI_MAP.items():
        text = text.replace(emoji, label)
    text = re.sub(r"https?://\S+|www\.\S+", " URL ", text)
    text = re.sub(r"@\w+", " USER ", text)
    text = re.sub(r"#(\w+)", r" \1 ", text)  # keep hashtag words for analysis
    text = re.sub(r"(.)\1{2,}", r"\1\1", text)  # reduce elongated spellings
    text = re.sub(r"\s+", " ", text).strip()
    return text

def tokenize(text):
    # Keeps Devanagari word sequences and Latin tokens separately.
    return re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?|[\u0900-\u097F]+|\d+", normalize_text(text).lower())

def detect_language(text):
    s = normalize_text(text)
    devanagari = len(re.findall(r"[\u0900-\u097F]", s))
    latin = len(re.findall(r"[A-Za-z]", s))
    hinglish_markers = {"hai","hain","nahi","nai","bahut","bohot","yaar","ka","ki","mein","me","acha","accha","mast","kya","paisa","vasool","ho","raha"}
    tokens = set(re.findall(r"[a-z]+", s.lower()))
    if devanagari >= 3 and latin >= 3:
        return "Code-mixed"
    if devanagari >= 3:
        return "Hindi"
    if tokens & hinglish_markers:
        return "Hinglish"
    return "English"

def segment_hashtags(text):
    # Lightweight camel-case and digit boundary segmentation; not a full word-break model.
    return re.sub(r"([a-z])([A-Z])", r"\1 \2", str(text))
