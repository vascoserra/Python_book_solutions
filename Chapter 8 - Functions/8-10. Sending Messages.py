def show_messages(messages):
    print("We gonna show the folowing messages: ")
    for message in messages:
        print(f"{message}")


def sended_messages(messages, sent_messages):
    print("\nWe sended this message: ")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = ['A vida é bela', 'Titanic foi ao fundo']
show_messages(messages)


sent_messages = []
sended_messages(messages[:], sent_messages)

print("\nFinal lists: ")
print(f"The original list : {messages}")
print(f"The copied list : {sent_messages}")
