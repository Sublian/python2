from gtts import gTTS
import os
 
tts = gTTS(text="El tóxico te esta llamando, contesta! El tóxico te llama, se está volviendo loco!!!", lang="es")
filename = "hello4.mp3"
tts.save(filename)
os.system(f"start {filename}")