#Городецкий Тимофей
#12.11.2026
#14:38
#Автоматическая регистрация на сайте

page = context.new_page()
page.goto('https://github.com/login')

# Interact with login form
page.get_by_label("Username or email address").fill("username")
page.get_by_label("Password").fill("password")
page.get_by_role("button", name="Sign in").click()
# Continue with the test 
