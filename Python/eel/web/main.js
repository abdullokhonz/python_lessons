const preLoad = document.getElementById('preloader');

window.addEventListener('load', function() {
    setTimeout(function() {
        preLoad.style.display = 'none';
    }, 3000);
});

let city = document.getElementById('city');
let miniWeather = document.getElementById('mini-weather');
let time = document.getElementById('time');
let batteryCharge = document.getElementById('battery-charge');

let info = document.getElementById('info');
let celsius = document.getElementById('celsius');

let voiceTheWeather = document.getElementById('voice-the-weather');

async function displayWeather() {
    info.innerHTML = '';

    let place = document.getElementById('location').value;
    let weather = await eel.get_weather(place)();

    info.innerHTML = weather;
    city.innerHTML = place;
}

function playAudioWeather() {
    voiceTheWeather.pause();

    voiceTheWeather.src = "audios/weather.mp3?t=" + new Date().getTime();

    voiceTheWeather.play();
}

async function displayWeatherCelsius() {
    celsius.innerHTML = '';

    let place = document.getElementById('location').value;
    let weatherCelsius = await eel.get_weather_celsius(place)();

    celsius.innerHTML = weatherCelsius + '°';
    miniWeather.innerHTML = weatherCelsius + '°';
}

async function displayTime() {
    await eel.get_current_time()().then(currentTime => { 
        time.innerHTML = currentTime; 
    });
}

async function displayBatteryCharge() {
    let charge = await eel.get_battery_charge()(); 

    batteryCharge.innerHTML = charge + '%';
}

setInterval(() => {
    displayTime();
    displayBatteryCharge();
}, 1000);

jQuery('#show').on('click', function() {
    displayWeather();
    displayWeatherCelsius();
    playAudioWeather();
});
