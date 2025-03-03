import librosa
import numpy as np
import soundfile as sf
import os

# Путь к файлу с песней
input_file = r"C:\Users\user\Downloads\1691811217-1691810967-farahmand-karimov-tantanai-khotiraho-2023-sw9fj8xu_9VbR29Pk.mp3"

# Загружаем аудиофайл
y, sr = librosa.load(input_file, mono=False)

# Если файл вдруг моно, создаём стерео-версию
if len(y.shape) == 1:
    y = np.array([y, y])

# Разделяем на mid/side
mid = (y[0] + y[1]) / 2
side = (y[0] - y[1]) / 2

# Настройка уровня вокала (mid). Например, 0.3 — это оставить 30% вокала.
vocal_level = 0.1

# Смешиваем mid (вокал) и side (музыка)
karaoke_left = side + mid * vocal_level
karaoke_right = side - mid * vocal_level

# Склеиваем обратно в стерео
karaoke = np.array([karaoke_left, karaoke_right])

# Путь для сохранения минуса
output_folder = r"D:\My files\Music\Minus"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Сохраняем результат
sf.write(os.path.join(output_folder, 'minus.wav'), karaoke.T, sr)

print("Готово! Минус сохранён как 'minus.wav'")
