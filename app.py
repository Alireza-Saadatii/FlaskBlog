from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Blog Home."


from mod_admin import admin

app.register_blueprint(admin)

from mod_admin import admin
app.register_blueprint(admin)


if __name__ == "__main__" :
    app.run(debug=True , host="0.0.0.0" , port=5000)