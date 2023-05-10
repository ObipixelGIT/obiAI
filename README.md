# obiAI
obiAI is a Python 3 OpenAI GPT Mic Audio Chat script.

## How the script works?
ObiAI is a Python 3 script that creates a simple chatbot that can listen to a user's voice input, convert the speech to text, respond to the user's input using OpenAI's text generation API, and speak the response aloud using a text-to-speech engine.

Here is a breakdown of the functionality:

- The script starts by importing necessary libraries such as os, openai, pyttsx3, speech_recognition, and emoji.
- The OpenAI API key is imported from a separate file called "openapikey".
- The text-to-speech engine is initialized using the pyttsx3 library.
- The speech recognition module and microphone are initialized using the speech_recognition library.
- A while loop is created to continuously listen for user input and respond to it.
Within the loop, the microphone is used to listen for the user's input, and Google's speech recognition service is used to convert the user's speech to text.
- If the user's input matches the exit phrase "I am done", the program will exit the loop and terminate.
- If the speech recognition service cannot understand the user's input, it will print a message to the console and continue listening for input.
- If the speech recognition service encounters an error, it will print a message to the console and continue listening for input.
- The user's input is added to the conversation history.
- OpenAI's text generation API is used to generate a response to the user's input.
- The response is extracted from the chatbot and spoken aloud using the text-to-speech engine.
- The response is also printed to the console.
- If an error occurs during the generation of the response, a friendly error message is printed to the console and the loop continues.

