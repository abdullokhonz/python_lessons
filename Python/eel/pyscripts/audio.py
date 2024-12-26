from gtts import gTTS


def weather_audio(text) -> gTTS:
    audio: str = "web/audios/weather.mp3"
    lang: str = "ru"

    sp: gTTS = gTTS(text=text, lang=lang, slow=False)

    return sp.save(audio)
