from flask import Flask

app = Flask(__name__)
app.secret_key = 'mekelcafay?siduri!'
from app import views
