# Городецкий Тимофей
# 15:20 
# 13.11.2026
def handle_route(route: Route) -> None:
    # Получить оригинальный ответ.
    response = route.fetch()
    # Добавить префикс к заголовку.
    body = response.text()
    body = body.replace("<title>", "<title>My prefix:")
    route.fulfill(
        # Передать все поля из ответа.
        response=response,
        # Переопределить тело ответа.
        body=body,
        # Принудительно установить тип контента как html.
        headers={**response.headers, "content-type": "text/html"},
    )

page.route("**/title.html", handle_route) 
