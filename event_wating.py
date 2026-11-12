#Городецкий Тимофей
#15:02
#12.11.2026

with page.expect_request("**/*logo*.png") as first:
  page.goto("https://wikipedia.org")
print(first.value.url)
