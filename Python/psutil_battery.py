import psutil

battery = psutil.sensors_battery()
percent = int(battery.percent)
print(f"Заряд батареи: {percent}%")

print(f"Заряд батареи: {psutil.sensors_battery().percent}%")
