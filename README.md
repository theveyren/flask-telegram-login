# Простая авторизация пользователей на вашем сайте
Лучший репозитори чтобы авторизовывать пользователей телеграмма! Вперёд самолётик, вперёд, телеграмм!
Что нужно чтобы всё заработало:
в `main.py` вписать все что нужно для работы с авторизацией:
```
app.jinja_env.globals.update(bot_id = REQUIRED) #айди бота из токена до знака ":"
app.jinja_env.globals.update(bot_name = REQUIRED) #имя вашего бота с приставкой bot
app.jinja_env.globals.update(domain = REQUIRED) #домен вашего сайта из /setdomain в BotFather (обычно http://127.0.0.1:5000)
```
Ну и конечно же библы:
`pip install quart`

Старку пж! По всем вопросам https://theveyren.tk/discord
Репозиторий обновляется, так чтоооо.....
