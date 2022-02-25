from quart import Quart, render_template, jsonify
from render import achievement, amiajoke, bad, calling, captcha, didyoumean, drake, facts, filter, floor, fml, jokeoverhead, opinion, pornhub, salty, scroll, shame, ship, what

app = Quart(__name__)

@app.route('/')
async def index():
    return jsonify({
        "endpoints": [
            "/achievement?text=text[&icon=int]",
            "/challenge?text=text[&icon=int]",
            "/amiajoke?image=url",
            "/bad?image=url",
            "/calling?text=text",
            "/captcha?text=text",
            "/didyoumean?top=text&bottom=text",
            "/drake?top=text&bottom=text",
            "/facts?text=text",
            "/floor?image=url&text=text",
            "/fml",
            "/jokeoverhead?image=url",
            "/trash?face=url&trash=url",
            "/pornhub?text=text&text2=text",
            "/salty?image=url",
            "/scroll?text=text",
            "/saa   hame?image=url",
            "/ship?user=url&user2=url",
            "/what?image=url"
        ],
        "credits": [
            "AlexFlipnote, argo0n, bentettmar"
        ]
    })

app.register_blueprint(achievement.blueprint)
app.register_blueprint(amiajoke.blueprint)
app.register_blueprint(bad.blueprint)
app.register_blueprint(calling.blueprint)
app.register_blueprint(captcha.blueprint)
app.register_blueprint(didyoumean.blueprint)
app.register_blueprint(drake.blueprint)
app.register_blueprint(facts.blueprint)
app.register_blueprint(filter.blueprint)
app.register_blueprint(floor.blueprint)
app.register_blueprint(fml.blueprint)
app.register_blueprint(jokeoverhead.blueprint)
app.register_blueprint(opinion.blueprint)
app.register_blueprint(pornhub.blueprint)
app.register_blueprint(salty.blueprint)
app.register_blueprint(scroll.blueprint)
app.register_blueprint(shame.blueprint)
app.register_blueprint(ship.blueprint)
app.register_blueprint(what.blueprint)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
