# llm_podcast

![Version](https://badgen.net/badge/version/1.0.0/blue)
![Python](https://badgen.net/badge/python/3.8%2B/blue)
![License](https://badgen.net/badge/license/MIT/green)
![Framework](https://badgen.net/badge/module/ollama/orange)

The LLM Podcast is a program where two LLMs have a conversation about any 
topic of the user's choosing.

This project makes two LLMs have a conversation about whatever the user chooses. 
Ollama is used to self-host the LLMs to facilitate a conversation, pyttsx3 is 
used to say what the LLMs output, and subprocess and threading is used to 
circumvent an error in the pyttsx3 module where after it finishes speaking, it 
hangs and stalls the program. It was tough to figure out where the hanging error 
was coming from, and it was even tougher to figure out how to fix it. I hope to 
be able to make this project more complex by creating a system for more than two 
LLMs to speak with each other. I would also like to add a feature where the user 
can have a conversation with the LLM out loud.

This project uses the libraries:
 - ollama
 - pyttsx3
 - subprocess
 - threading

Using the project requires downloading Ollama, using Ollama to download the 
llama3.2:3b model, and running main.py in your IDE of choice with the
correct libraries installed. Once the project is running, it should prompt 
the user for something that the LLMs should talk about. There is a sample 
prompt in the multi-line string at the top of main.py. Once the prompt is 
input, the first LLM should start streaming the output to the console. 
Once the first LLM's response has been streamed to the console, 

MIT License

Copyright (c) [2025] [Marshall Pigford]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
