messages_list = ['Hi there', 'how are you', 'what are you doing?']
sent_messages=[]

def send_messages(messages_list, sent_messages):
	while messages_list:
		current_message = messages_list.pop()
		sent_messages.append(current_message)


send_messages(messages_list[:], sent_messages) #notice we're sending copy of messages_list to the function

print(sent_messages)
print(messages_list) #even though we've popped all the messages, this will still be the same as the original list 