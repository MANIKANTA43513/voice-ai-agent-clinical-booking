
from langdetect import detect

def detect_language(text):

    try:
        lang = detect(text)
    except:
        lang = "en"

    if lang == "hi":
        return "Hindi"

    if lang == "ta":
        return "Tamil"

    return "English"
