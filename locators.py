#Городецкий Тимофей
#09.11.2026
#16:38
#Создание превого локатора благодоря Codegen


import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.locator("html").click()
    page.get_by_placeholder("What needs to be done?").click(button="right")
    page.get_by_placeholder("What needs to be done?").fill("'assert visibility'")
    page.get_by_placeholder("What needs to be done?").press("Enter")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
 
