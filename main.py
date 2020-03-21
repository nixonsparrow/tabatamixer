from flask import Flask, escape, request, render_template, url_for
from tabatamixer import create_tabata_set, tabata_music

app = Flask(__name__)


@app.route('/')
@app.route('/tabata')
def home():
    while True:
        tabata_song = tabata_music()
        exercises = create_tabata_set()
        return render_template('tabata.html', exercises=exercises, tabata_song=tabata_song)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
