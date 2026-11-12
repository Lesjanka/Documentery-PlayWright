#Городецкий Тимофей
#12.11.2026
#14:54
#Соответствено выводит местоположение
context = browser.new_context(
  geolocation={"longitude": 41.890221, "latitude": 12.492348},
  permissions=["geolocation"]
)
