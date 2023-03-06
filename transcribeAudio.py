import os
import openai
import json
openai.api_key = os.getenv("OPENAI_API_KEY")
# using audio file from the interwebs for now, need to work through how this is retrieved in real time
audio_file = open("C:/Users/charl/Downloads/timtube__talking.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

newString = transcript["text"]
print(newString)


# Success! The response includes the correct transcription of "Are you alright?"
# It even includes punctuation, that's pretty sick!
# Next step: determine what the best format for this response to be in is so it can be POSTed into other endpoints for processesing
# See: completions to start. (https://platform.openai.com/docs/api-reference/completions)

completion = openai.Completion.create(
  model="text-davinci-003",
  prompt="The following is a conversation between a human and a smart, friendly, powerful AI assistant. \nHuman: Hello! I am your friend the human.\nAI: Greetings! It is I, your clever AI assistant.\nHuman: "+newString+"\nAI: ",
  max_tokens=7,
  temperature=0.5
)

print(completion.choices[0].text)

# Awesome! I'm now able to have the AI respond to the deciphered audio based on the provided prompt.
# Next, I want to revisit how I am capturing the audio and see how I can make this more viable to use "on-the-fly"