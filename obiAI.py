# -*- coding: utf-8 -*-
# Author : Dimitrios Zacharopoulos
# All copyrights to Obipixel Ltd
# 10 May 2023

#/usr/bin/python3


# Print ASCII art
print("""
 ██████╗ ██████╗ ██╗ █████╗ ██╗
██╔═══██╗██╔══██╗██║██╔══██╗██║
██║   ██║██████╔╝██║███████║██║
██║   ██║██╔══██╗██║██╔══██║██║
╚██████╔╝██████╔╝██║██║  ██║██║
 ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝
""")

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