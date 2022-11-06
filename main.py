from quart import Quart, render_template, request, redirect, url_for, session

app = Quart(__name__)
app.config['SECRET_KEY'] = "TELEGRAM-LOGIN"
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.jinja_env.globals.update(bot_id = REQUIRED) #Айди бота из токена до знака ":"
app.jinja_env.globals.update(bot_name = REQUIRED) #Имя вашего бота с приставкой bot
app.jinja_env.globals.update(domain = REQUIRED) #Домен вашего сайта из /setdomain в BotFather (обычно http://127.0.0.1:5000)

@app.before_request
async def make_session_permanent():
    session.permanent = True

async def template(tmpl_name, **kwargs):
    telegram = False
    user_id = session.get('user_id')
    username = session.get('name')
    photo = session.get('photo')

    if user_id:
        telegram = True

    return await render_template(tmpl_name,
                           telegram = telegram,
                           user_id = user_id,
                           name = username,
                           photo = photo,
                           **kwargs)

@app.route("/")
async def index():
    return await template("telegram.html")

@app.route("/logout")
async def logout():
    session.pop("user_id")
    session.pop("name")
    session.pop("photo")

    return redirect(url_for('index'))

@app.route("/login")
async def login():
    user_id = request.args.get("id")
    first_name = request.args.get("first_name")
    photo_url = request.args.get("photo_url")

    session['user_id'] = user_id
    session['name'] = first_name
    session['photo'] = photo_url

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug = True)