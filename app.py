from os import environ
from sandman2 import get_app
from flask_cors import CORS

app = get_app(environ['DATABASE_URL'])
cor = CORS()
cor.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)