chat_history = []

def remember(message):
    chat_history.append(message)

def get_last_user_message():
    return chat_history[-1] if chat_history else None