#
#
#
#

# СОздать контекст с темой
context = browser.new_context(
  color_scheme='dark' # or 'light'
)

#Создание страницы с темной темой
page = browser.new_page(
  color_scheme='dark' # or 'light'
)

# Изменение схемы на тему
page.emulate_media(color_scheme='dark')

# ?
page.emulate_media(media='print')
