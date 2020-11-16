import pyttsx3

speech = pyttsx3.init()
#1 - you can copy/paste this comment bellow 
# to find out what voices are avaliable on your PC

speech.setProperty("rate", 120)
speech.setProperty("volume",1)

# Use another voice
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
speech.setProperty("voice", voice_id)

speech.say("Enter your text here.")
speech.runAndWait()




"""
#1 - use this one to find out what voices are avaliable on your PC
voices = speech.getProperty('voices') 

for voice in voices: 
	# to get the info. about various voices in our PC 
	print("Voice:") 
	print("ID: %s" %voice.id) 
	print("Name: %s" %voice.name) 
	print("Age: %s" %voice.age) 
	print("Gender: %s" %voice.gender) 
	print("Languages Known: %s" %voice.languages) 

"""

