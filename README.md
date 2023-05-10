# obiAI
obiAI is a Python 3 OpenAI GPT Mic Audio Chat script with a text-to-speech-to-text-speech engine.

## How the script works?
ObiAI is a Python 3 script that creates a simple chatbot that can listen to a user's voice input, convert the speech to text, respond to the user's input using OpenAI's text generation API, and speak the response aloud using a text-to-speech engine.

Here is a breakdown of the functionality:

- The script starts by importing necessary libraries such as os, openai, pyttsx3, speech_recognition, and emoji.
- The OpenAI API key is imported from a separate file called "openapikey". You will need to get an API key from GPT and add it to a file called "openapikey".
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

## Preparation

The following Python modules must be installed:
```bash
pip3 install openai, pyttsx3, SpeechRecognition, emoji
```

## Permissions

Ensure you give the script permissions to execute. Do the following from the terminal:
```bash
sudo chmod +x obiAI.py
```

## Usage
*** When obiAI is listening, just ask GPT what you want to know, and then wait for GPT to respond :-)
```bash
 sudo python3 obiAI.py                                                                                     
Password:

 ██████╗ ██████╗ ██╗ █████╗ ██╗
██╔═══██╗██╔══██╗██║██╔══██╗██║
██║   ██║██████╔╝██║███████║██║
██║   ██║██╔══██╗██║██╔══██║██║
╚██████╔╝██████╔╝██║██║  ██║██║
 ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝


👂 Listening...
```


## Sample script
```python
# Import required libraries
import os
import openai
import pyttsx3
import speech_recognition as sr
import emoji

# Import the OpenAI API key from a separate file
from openapikey import APIKEY

# Set the API key for OpenAI
openai.api_key = APIKEY

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognition module and microphone
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)

# Print a list of available microphones
#print(sr.Microphone.list_microphone_names())

# Set up variables for the conversation and user name
conversation = ""
user_name = "Dimitrios"

# Continuously listen for user input and respond
while True:
    # Use the microphone to listen for user input
    with mic as source:
        print("\n" + emoji.emojize(":ear:") + " Listening...\n")
        r.adjust_for_ambient_noise(source, duration=0.1)
        audio = r.listen(source)
    print("No longer Listening...")

    # Use Google's speech recognition service to convert user's speech to text
    try:
        user_input = r.recognize_google(audio)
        print("User Input: " + user_input)

        # Check if user input matches exit phrase
        if user_input == "I am done":
            print("Exiting program...")
            break
    
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
        continue
    except sr.RequestError as e:
        print("Could not request results from speech recognition service; {0}".format(e))
        continue

    # Add user input to conversation history
    prompt = user_name + ": " + user_input + "\n:"
    conversation += prompt

    # Use OpenAI API to generate a response
    try:
        response = openai.Completion.create(engine='text-davinci-003', prompt=conversation, temperature=0.9, max_tokens=150)
        response_str = response["choices"][0]["text"].replace("\n", "")

        # Extract the response from the chatbot and speak it aloud
        response_str_list = response_str.split(user_name + ": ", 1)[0].split("Dimitrios: ", 1)
        if len(response_str_list) > 1:
            response_str = response_str_list[1]
        else:
            response_str = ""

        conversation += response_str + "\n"

        # also respond using an emoji speech baloon
        print("\n" + emoji.emojize(":speech_balloon:") + " " + response_str)

        # Generate a new response incorporating the chat history and speak it aloud
        response = openai.Completion.create(engine='text-davinci-003', prompt=conversation, temperature=0.9, max_tokens=150)
        response_str = response["choices"][0]["text"].replace("\n", "")

        engine.say(response_str)  # Add the text response to the text-to-speech engine's queue
        engine.runAndWait()  # Instruct the text-to-speech engine to start speaking the queued text out loud
        print(response_str)  # Print the text response to the console, so the user can see it even if they can't hear it

    # If an error occurs in the previous try block, catch the exception and assign it to the variable e
    except Exception as e:

        # Print a friendly error message to the console, using string formatting to include the specific error message
        print("Error occurred while processing user input: {0}".format(e))

        # Continue the loop, so that the chatbot can keep running and the user can continue to interact with it
        continue
```

## Disclaimer
"The scripts in this repository are intended for authorized security testing and/or educational purposes only. Unauthorized access to computer systems or networks is illegal. These scripts are provided "AS IS," without warranty of any kind. The authors of these scripts shall not be held liable for any damages arising from the use of this code. Use of these scripts for any malicious or illegal activities is strictly prohibited. The authors of these scripts assume no liability for any misuse of these scripts by third parties. By using these scripts, you agree to these terms and conditions."

## License Information

This library is released under the [Creative Commons ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/). You are welcome to use this library for commercial purposes. For attribution, we ask that when you begin to use our code, you email us with a link to the product being created and/or sold. We want bragging rights that we helped (in a very small part) to create your 9th world wonder. We would like the opportunity to feature your work on our homepage.

