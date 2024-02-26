from flask import Flask, render_template, request
from database import get_entries, get_recent_entries, add_entry
import datetime, time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    now = datetime.datetime.now()
    if ('date' in request.form.keys()) and ('entry' in request.form.keys()):
        add_entry(request.form['date'], request.form['entry'], int(time.mktime(now.timetuple())))
    recent_entries = get_recent_entries()
    return render_template("index.html", rec_ent=recent_entries)
