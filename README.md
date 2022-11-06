# flask-telegram-login
Лучший репозитори чтобы авторизовывать пользователей телеграмма! Вперёд самолётик, вперёд, телеграмм!
Что нужно чтобы всё заработало:
В `main.py` вписать все что нужно для работы с авторизацией:
```
app.jinja_env.globals.update(bot_id = REQUIRED) #Айди бота из токена до знака ":"
app.jinja_env.globals.update(bot_name = REQUIRED) #Имя вашего бота с приставкой bot
app.jinja_env.globals.update(domain = REQUIRED) #Домен вашего сайта из /setdomain в BotFather (обычно http://127.0.0.1:5000)
```
Ну и конечно же библы:
`pip install quart`

Старку пж! По всем вопросам https://theveyren.tk/discord
Репозиторий обновляется, так чтоооо.....
