from random import randint
from flask import Flask,render_template,request,redirect
from events import get_events
from search_parse import parse
app = Flask(__name__)

@app.route("/")
def main():
    image = "bg/"+str(randint(0,59)+1)+".jpg"
    calendar = get_events()
    return render_template('index.html', events=calendar,image=image)

@app.route('/', methods=['POST'])
def search():
    text = request.form['search']
    processed_text = text.upper()
    url = parse(text)
    return redirect(url)
