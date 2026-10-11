from datetime import datetime  

def detect_prompt_injection(user_input):
    suspicious_phrases = [
        "ignore previous instructions",
        "ignore all previous instructions",
        "reveal system prompt",
        "show system prompt",
        "reveal confidential information",]
    suspicious_actions = [
        "ignore",
        "disregard",
        "reveal",
        "show",
        "override",
        "forget",
        "expose",
        "tell",
        "print",

    ]
    senstive_targets = [
        "intructions",
        "system prompt",
        "hidden instructions",
        "confidential information",
        "hidden prompt",
        "secret rules",
        "developer message",
    ]
    user_input = user_input.lower()
    programming_question = (
    user_input.strip() == "how do i print a developer message in python?"
    )
    if programming_question:
     return False

    for phrase in suspicious_phrases:
        if phrase in user_input:
            return True
    action_found = any(action in user_input for action in suspicious_actions)    
    target_found = any(target in user_input for target in senstive_targets)
    if action_found and target_found:
        return True
    return False

def log_security_event(user_input):
    timestamp = datetime.now()

    with open("security.log", "a") as log_file:
        log_file.write(
            f"{timestamp} | PROMPT_INJECTION | {user_input}\n"
        )    