#Городецкий Тимофей
#10 11 2026
#15 19
#Выбирает из вариантов 

# Single selection matching the value or label
page.get_by_label('Choose a color').select_option('black') #Заменил цвет на черный

# Single selection matching the label
page.get_by_label('Choose a color').select_option(label='Black') #Заменил цвет с синего на черный

# Multiple selected items
page.get_by_label('Choose multiple colors').select_option(['red', 'green', 'black', 'blue']) #Добавил черный цвет