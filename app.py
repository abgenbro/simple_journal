from flask import Flask, render_template, request
from database import get_entries, add_entry

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if ('date' in request.form.keys()) and ('entry' in request.form.keys()):
        add_entry(request.form['date'], request.form['entry'])
    recent_entries = get_entries(5)
    return render_template("index.html", rec_ent=recent_entries)

if __name__ == '__main__':
    app.run(debug=True)