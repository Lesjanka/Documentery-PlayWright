#Городецкий Тимофей
#12.11.2026
#14:47
#Имитация какого либо устройства с его фишками

from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    redmi_note_s14 = playwright.devices['Redmi Note S14'] #Заменил iPhone 13 на прекрасный Redmi Note S14
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(
        **redmi_note_s14,
    )

with sync_playwright() as playwright:
    run(playwright)
