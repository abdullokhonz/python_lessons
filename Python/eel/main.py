from eel import init, start, expose
from pyowm import OWM
from time import strftime
from psutil import sensors_battery
from pyscripts.audio import weather_audio
from pyscripts.screen_size import screen_size

owm: OWM = OWM("6d00d1d4e704068d70191bad2673e0cc")


@expose
def get_weather(place) -> str:
    city: str = place
    mgr: owm = owm.weather_manager()

    try:
        observation: owm = mgr.weather_at_place(city)
        w: owm = observation.weather
        temp: float = w.temperature("celsius")["temp"]

        text: str = f'В городе {city} сейчас {round(temp)} градусов!'

        weather_audio(text)

        return text
    except Exception as e:
        text: str = f"Не удалось получить данные погоды: {e}"

        weather_audio(text)

        return text


@expose
def get_weather_celsius(place) -> float:
    city: str = place

    mgr: owm = owm.weather_manager()
    observation: owm = mgr.weather_at_place(city)
    w: owm = observation.weather
    temp: float = w.temperature("celsius")["temp"]

    return round(temp)


@expose
def get_current_time() -> strftime:
    return strftime("%H:%M")


@expose
def get_battery_charge() -> int:
    battery: sensors_battery = sensors_battery()
    percent: int = int(battery.percent)

    return percent


init("web")

start("main.html", size=screen_size())
