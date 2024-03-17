def show_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Message: {current_message}")
        sent_messages.append(current_message)
        
def send_messages(sent_messages):
    print("\nThe following messages have been sent:")
    for sent_message in sent_messages:
        print(sent_message)

messages = ["Hello", "You're welcome!", "Nice!", "git gud"]
sent_messages = []

show_messages(messages, sent_messages)
send_messages(sent_messages)