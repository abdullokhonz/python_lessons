# import os
# import psutil
#
# processes_to_kill: list = ["WidgetService.exe"]
#
#
# def kill_processes(process_list):
#     for proc in psutil.process_iter(["pid", "name"]):
#         if proc.info["name"] in process_list:
#             try:
#                 os.kill(proc.info["pid"], 9)
#                 print(f"Процесс {proc.info["name"]} завершён.")
#             except Exception as e:
#                 print(f"Не удалось завершить процесс {proc.info['name']}: {e}")
#
#
# if __name__ == "__main__":
#     kill_processes(processes_to_kill)

# import os
# import psutil
#
# # Список ключевых слов для процессов, которые нужно завершить
# keywords_to_kill = [
#     "WhatsApp",
#     "Widget",
#     "Xbox",
#     "Мини-приложения",
#     "Экран Блокировки",
# ]
#
#
# def kill_processes_by_keywords(keywords):
#     for proc in psutil.process_iter(['pid', 'name']):
#         proc_name = proc.info['name'].lower()  # Приводим имя процесса к нижнему регистру
#         if any(keyword.lower() in proc_name for keyword in keywords):
#             try:
#                 os.kill(proc.info['pid'], 9)
#                 print(f"Процесс {proc.info['name']} завершён.")
#             except Exception as e:
#                 print(f"Не удалось завершить процесс {proc.info['name']}: {e}")
#
#
# if __name__ == "__main__":
#     kill_processes_by_keywords(keywords_to_kill)
