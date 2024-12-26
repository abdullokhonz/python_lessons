from gtts import gTTS

audio = 'audio.mp3'
language = 'ru'
sp = gTTS(text='Я твой дом шатал!', lang=language, slow=False)
sp.save(audio)
