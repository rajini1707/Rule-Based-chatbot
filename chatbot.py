# Rule-Based AI Chatbot - Project 1

responses = {
    "hello"     : "Hi there! How can I help you?",
    "hi"        : "Hey! Nice to meet you.",
    "how are you" : "I'm doing great, thanks for asking!",
    "what is ai"  : "AI is making machines think like humans!",
    "your name"   : "I am RuleBot, your AI assistant.",
    "bye"         : "Goodbye! See you next time.",
    "exit"        : "Goodbye! See you next time.",
}

print("RuleBot: Hello! Type 'bye' to exit.\n")

# HEARTBEAT - Infinite loop (runs until kill command)
while True:

    # PHASE 1 - Input & Sanitization
    raw_input_text = input("You: ")
    clean_input = raw_input_text.lower().strip()

    # EXIT STRATEGY - Clean break command
    if clean_input in ("bye", "exit"):
        print("RuleBot: Goodbye! See you next time.")
        break

    # PHASE 2 - Lookup using .get() method
    reply = responses.get(clean_input, "I don't understand. Try: hello, hi, bye")

    # PHASE 3 - Output
    print("RuleBot:", reply)