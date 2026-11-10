#Городецкий Тимофей
#10.11.2026
#15:10
#Позволяет автоматизировать браузер

from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()
# Use playwright.chromium, playwright.firefox or playwright.webkit
# Pass headless=False to launch() to see the browser UI
browser = playwright.chromium.launch()
page = browser.new_page()
page.goto("https://github.com/Lesjanka") #Заменил ссылку на свой профиль ГитХаба
page.screenshot(path="example.png")
browser.close()
playwright.stop()

