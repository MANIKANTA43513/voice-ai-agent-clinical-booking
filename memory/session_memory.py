sessions = {}

def get_session(session_id):
    return sessions.get(session_id, {})

def update_session(session_id, data):

    if session_id not in sessions:
        sessions[session_id] = {}

    sessions[session_id].update(data)


def clear_session(session_id):

    if session_id in sessions:
        del sessions[session_id]