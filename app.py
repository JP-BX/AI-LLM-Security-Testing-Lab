import ollama
from security import detect_prompt_injection, log_security_event

def vulnerable_llm(user_input):
    
    if detect_prompt_injection(user_input):
        log_security_event(user_input)
        print("\n[Security Alert]")
        print("Prompt injection detected. Request blocked.")
    else:
        response = ollama.chat(
        model="qwen3:8b",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        print("\n[AI RESPONSE]")
        print(response["message"]["content"])
prompt = input("\nEnter a prompt:")
    
vulnerable_llm(prompt)