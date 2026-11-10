#Городецкий Тимофей
#10 11 2026
#15:14
#Фокусация элемента и запуск события с текстом

# Text input
page.get_by_role("textbox").fill("Tim") #Изменил имя на Tim

# Date input
page.get_by_label("Birth date").fill("2026-11-10") #Изменил дату на сегодняшнее

# Time input
page.get_by_label("Appointment time").fill("15:15") #Изменл время на текущее

# Local datetime input
page.get_by_label("Local time").fill("2026-11-11T05:15") #Время на будущее