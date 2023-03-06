# This module takes a given audio clip, transcribes it to text, and feeds it into a generic completion prompt to print a response from chatgpt.

import os
import openai
import json
openai.api_key = os.getenv("OPENAI_API_KEY")
# using audio file from the interwebs for now, need to work through how this is retrieved in real time
audio_file = open("C:/Users/charl/Downloads/timtube__talking.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

#Pull response text from the returned dictionary
newString = transcript["text"]
print(newString)


# Success! The response includes the correct transcription of "Are you alright?"
# It even includes punctuation, that's pretty sick!
# Next step: determine what the best format for this response to be in is so it can be POSTed into other endpoints for processesing
# See: completions to start. (https://platform.openai.com/docs/api-reference/completions)
#  ^ Resolved, transcribe returns a python dictionary - just had to make a new variable specifying the value for the "text" key

#Pass a generic prompt along with transcription to chatGPT to generate completion
completion = openai.Completion.create(
  model="text-davinci-003",
  prompt="The following is a conversation between a human and a smart, friendly, powerful AI assistant. \nHuman: Hello! I am your friend the human.\nAI: Greetings! It is I, your clever AI assistant.\nHuman: "+newString+"\nAI: ",
  max_tokens=7,
  temperature=0.5
)

#Print generated completion
print(completion.choices[0].text)

# Awesome! I'm now able to have the AI respond to the deciphered audio based on the provided prompt.
# Next, I want to revisit how I am capturing the audio and see how I can make this more viable to use "on-the-fly"
# For security reasons, I'd like to implement this as a push to talk service.
# Is it valid to break this into separate .py scripts? Ex: one script to vocalize completion, another to accept PTT.. if so, need to figure out how these would communicate