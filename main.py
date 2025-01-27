from ollama import chat
import subprocess
import threading

"""A good one: You are an AI podcast host! You are talking with your AI co-host about Jesus. 
Explore the intricacies of this topic and exery so often dig deeper into the topic so that you 
never run out of things to say. After you finish speaking, wait for your AI co-host to respond. 
Make sure to say lots so that your co-host can have enough time to think about what to say. What 
do you have to say to start off the conversation!

"""

def run_speak_script(stream_output):
    subprocess.call(["python3", "speak.py", stream_output])

# Grab LLM input
print('What would you like the AI to talk about? : ', end = '')
user_input = input()

# Initialize the message history
message_history1 = ''
message_history2 = 'You are an AI co-host to a podcast. Wait for your AI co-host to start off and just keep the conversation going!\n'

# Build the whole prompt
prompt1 = f'This is the message history: {message_history1} \nYou should respond to this: {user_input}'

# Create a stream for LLM output
stream1 = chat(
    model = 'llama3.2:3b', 
    messages = [{'role': 'user', 'content': prompt1}], 
    stream = True
)

# Stream the LLM output
print('\nBot1: ', end='')
stream_output1 = ''
for chunk in stream1:
    print(chunk['message']['content'], end = '', flush = True)
    stream_output1 += chunk['message']['content']

# Say the output
thread = threading.Thread(target = run_speak_script, args = (stream_output1,))
thread.start()

# Save response to the message history
message_history1 += f'You said: {stream_output1}\n'
message_history2 += f'Your friend said: {stream_output1}\n'

# Inputting the 1st LLM's output into the 2nd LLM
prompt2 = f'This is the message history: {message_history2} \nYou should respond to this: {stream_output1}'

while True:

    # Create a stream for LLM output
    stream2 = chat(
        model = 'llama3.2:3b', 
        messages = [{'role': 'user', 'content': prompt2}], 
        stream = True
    )

    # Stream the LLM output
    print('\nBot2: ', end='')
    stream_output2 = ''
    for chunk in stream2:
        print(chunk['message']['content'], end = '', flush = True)
        stream_output2 += chunk['message']['content']

    # Wait for the previous thread to stop
    thread.join()

    # Say the output
    thread = threading.Thread(target = run_speak_script, args = (stream_output1,))
    thread.start()

    # Saving LLM response to message history
    message_history1 += f'Your friend said: {stream_output2}\n'
    message_history2 += f'You said: {stream_output2}\n'

    # Build the whole prompt
    prompt1 = f'This is the message history: {message_history1} \nYou should respond to this: {user_input}'

    # Create a stream for LLM output
    stream1 = chat(
        model = 'llama3.2:3b', 
        messages = [{'role': 'user', 'content': prompt1}], 
        stream = True
    )

    # Stream the LLM output
    print('\nBot1: ', end='')
    stream_output1 = ''
    for chunk in stream1:
        print(chunk['message']['content'], end = '', flush = True)
        stream_output1 += chunk['message']['content']
    
    # Wait for the previous thread to stop
    thread.join()

    # Say the output
    thread = threading.Thread(target = run_speak_script, args = (stream_output1,))
    thread.start()

    # Save response to the message history
    message_history1 += f'You said: {stream_output1}\n'
    message_history2 += f'Your friend said: {stream_output1}\n'

    # Inputting the 1st LLM's output into the 2nd LLM
    prompt2 = f'This is the message history: {message_history2} \nYou should respond to this: {stream_output1}'