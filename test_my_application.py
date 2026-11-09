#Городецкий Тимофей
#09.11.2026
#16:47
#

from playwright.sync_api import Page

def test_visit_admin_dashboard(page: Page):
    page.goto("/admin")
from playwright.sync_api import Page, BrowserContext
from pytest_playwright.pytest_playwright import CreateContextCallback

def test_foo(page: Page, new_context: CreateContextCallback) -> None:
    page.goto("https://example.com")
    context = new_context()
    page2 = context.new_page()

