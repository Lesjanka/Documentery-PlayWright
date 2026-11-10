#Городецкий Тимофей
#10.11 2026
#15:06
#Позволяет делать скриншот

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()
    page.goto("https://github.com/Lesjanka") #Заменил ссылку на свой профиль ГитХаба
    page.screenshot(path="example.png")
    browser.close()

