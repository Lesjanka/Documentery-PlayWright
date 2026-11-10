#Городецкий Тимофей
#10.11.2026
#15:02
#Позволяет запускать любой браузер на выбор

import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://github.com/Lesjanka") #Заменил ссылку на свой профиль ГитХаба
        print(await page.title())
        await browser.close()

asyncio.run(main())
