#Городецкий Тимофей
#09.11.2026
#16:26
#Использование приспособлений
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("before the test runs")

    page.goto("https://github.com/Lesjanka")
    yield
    
    print("after the test runs")

def test_main_navigation(page: Page):
    expect(page).to_have_url("https://github.com/Lesjanka")
