#Городецкий Тимофей
#09.11.2026
#16:51
#Использование пользовательский рамзер области просмотра 

import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }