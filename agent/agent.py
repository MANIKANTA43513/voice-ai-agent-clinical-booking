import json

def agent_reasoning(user_text):

    text = user_text.lower()

    intent = "unknown"
    doctor = ""
    date = ""
    time = ""

    if "book" in text:
        intent = "book"

    if "cancel" in text:
        intent = "cancel"

    if "cardiologist" in text:
        doctor = "cardiologist"

    if "tomorrow" in text:
        date = "tomorrow"

    # time detection
    if "10" in text:
        time = "10:00"

    if "14" in text or "2 pm" in text:
        time = "14:00"

    if "16" in text or "4 pm" in text:
        time = "16:00"

    agent_output = {
        "intent": intent,
        "doctor": doctor,
        "date": date,
        "time": time
    }

    return json.dumps(agent_output)