import threading
import webbrowser
from datetime import date
from flask import Flask, flash, redirect, render_template, request, url_for
import treningi as db

app = Flask(__name__)
app.secret_key = "ewidencja_treningow"


@app.route("/")
def index():
    workout_list = db.get_workouts()
    statistics = db.calculate_statistics()
    
    date_from = request.args.get("data_od", "")
    date_to = request.args.get("data_do", "")
    
    range_stats = None
    if date_from and date_to:
        range_stats = db.calculate_range_statistics(date_from, date_to)
        
    return render_template(
        "index.html",
        treningi=workout_list,
        statystyki=statistics,
        stats_zakresu=range_stats,
        data_od=date_from,
        data_do=date_to,
        today=date.today().isoformat(),
    )


@app.route("/dodaj", methods=["POST"])
def dodaj():
    workout_date = request.form.get("data", "")
    workout_type = request.form.get("typ", "")
    duration = request.form.get("czas", "")
    calories = request.form.get("kalorie", "")

    success, message = db.add_workout(
        workout_date, workout_type, duration, calories
    )
    flash(message, "success" if success else "error")
    return redirect(url_for("index"))


@app.route("/usun/<int:index>")
def usun(index):
    success, message = db.delete_workout(index)
    flash(message, "success" if success else "error")
    return redirect(url_for("index"))


def open_browser():
    webbrowser.open("http://127.0.0.1:8080")


if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start()
    print("Uruchamianie aplikacji... Przeglądarka otworzy się automatycznie.")
    app.run(host="0.0.0.0", port=8080, debug=False)