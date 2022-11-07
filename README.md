# Простая авторизация пользователей на вашем сайте
Что нужно чтобы всё заработало:

в `main.py` вписать все что нужно для работы с авторизацией:

```
app.jinja_env.globals.update(BOTID = REQUIRED) #айди бота из токена до знака ":"
app.jinja_env.globals.update(BOTNAME = REQUIRED) #имя вашего бота с приставкой bot
app.jinja_env.globals.update(BOTDOMAIN = REQUIRED) #домен вашего сайта из /setdomain в BotFather (обычно http://127.0.0.1:5000)
```

Поменяйте домен сайта на `http://127.0.0.1:5000` (для теста конечно же) в BotFather через команду `/setdomain`:

![Авторизация через телеграм](https://media.discordapp.net/attachments/993073713501196348/1039229083495698462/image.png)

Также скачайте блин фласк: `pip install flask`

Старку пж! По всем вопросам https://theveyren.tk/discord

Репозиторий обновляется, так чтоооо...
