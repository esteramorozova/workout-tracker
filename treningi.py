import json
import os
from datetime import datetime

FILE_PATH = "treningi.json"

# Słownik spalania kalorii na minutę dla różnych typów treningów
KCAL_BURN_PER_MIN = {
    "Bieganie": 10,
    "Siłownia": 6,
    "Rower": 8,
    "Basen": 9,
    "Spacer": 4,
    "Inny": 5
}

def load_workouts():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_workouts(workouts):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(workouts, f, ensure_ascii=False, indent=2)

def add_workout(date_str, workout_type, duration, calories):
    """Dodaje nowy trening. Zwraca (True, komunikat) lub (False, blad)."""
    if not date_str:
        date_str = datetime.today().strftime("%Y-%m-%d")
    
    try:
        workout_date = datetime.strptime(date_str, "%Y-%m-%d")
        # WALIDACJA: Blokada dat przed 1 stycznia 2000 roku
        min_date = datetime(2000, 1, 1)
        if workout_date < min_date:
            return False, "Data nie może być wcześniejsza niż 01.01.2000 r."
    except ValueError:
        return False, "Niepoprawny format daty."

    if not workout_type or not workout_type.strip():
        return False, "Typ treningu nie może być pusty."

    try:
        duration = int(duration)
        if duration <= 0:
            raise ValueError
    except ValueError:
        return False, "Czas musi być liczbą całkowitą większą od 0."

    # Automatyczne wyliczanie kalorii
    if not calories or str(calories).strip() == "" or int(calories) == 0:
        factor = KCAL_BURN_PER_MIN.get(workout_type.strip(), 5)
        calories = duration * factor
    else:
        try:
            calories = int(calories)
            if calories < 0:
                raise ValueError
        except ValueError:
            return False, "Kalorie muszą być liczbą nieujemną."

    workouts = load_workouts()
    
    workouts.append({
        "date": date_str, 
        "type": workout_type.strip(), 
        "duration": duration, 
        "calories": calories
    })
    save_workouts(workouts)
    return True, f"Trening został pomyślnie dodany!"

def get_workouts():
    workouts = load_workouts()
    # Sortowanie po angielskim kluczu "date"
    return sorted(workouts, key=lambda w: w["date"], reverse=True)

def calculate_statistics():
    workouts = load_workouts()
    if not workouts:
        return None

    now = datetime.today()
    current_year = now.year
    current_month = now.month
    current_week = now.isocalendar()[1] 

    stats = {
        "total": {"count": 0, "kcal": 0, "duration": 0},
        "yearly": {"count": 0, "kcal": 0, "duration": 0},
        "monthly": {"count": 0, "kcal": 0, "duration": 0},
        "weekly": {"count": 0, "kcal": 0, "duration": 0}
    }

    type_counts = {}

    for w in workouts:
        workout_date = datetime.strptime(w["date"], "%Y-%m-%d")
        
        stats["total"]["count"] += 1
        stats["total"]["kcal"] += w["calories"]
        stats["total"]["duration"] += w["duration"]
        
        type_counts[w["type"]] = type_counts.get(w["type"], 0) + 1

        if workout_date.year == current_year:
            stats["yearly"]["count"] += 1
            stats["yearly"]["kcal"] += w["calories"]
            stats["yearly"]["duration"] += w["duration"]

            if workout_date.month == current_month:
                stats["monthly"]["count"] += 1
                stats["monthly"]["kcal"] += w["calories"]
                stats["monthly"]["duration"] += w["duration"]
               
                if workout_date.isocalendar()[1] == current_week:
                    stats["weekly"]["count"] += 1
                    stats["weekly"]["kcal"] += w["calories"]
                    stats["weekly"]["duration"] += w["duration"]

    favorite_type = max(type_counts, key=type_counts.get) if type_counts else "Brak"
    total_count = stats["total"]["count"]
    total_duration = stats["total"]["duration"]
    
    return {
        "total": stats["total"],
        "yearly": stats["yearly"],
        "monthly": stats["monthly"],
        "weekly": stats["weekly"],
        "hours": total_duration // 60,
        "minutes": total_duration % 60,
        "avg_duration": round(total_duration / total_count, 1),
        "avg_calories": round(stats["total"]["kcal"] / total_count, 1),
        "favorite": favorite_type,
        "favorite_count": type_counts.get(favorite_type, 0)
    }

def calculate_range_statistics(date_from, date_to):
    workouts = load_workouts()
    if not date_from or not date_to:
        return None

    try:
        from_dt = datetime.strptime(date_from, "%Y-%m-%d")
        to_dt = datetime.strptime(date_to, "%Y-%m-%d")
    except ValueError:
        return None

    results = {"count": 0, "duration": 0, "kcal": 0, "avg_duration": 0, "type_breakdown": {}}

    for w in workouts:
        workout_date = datetime.strptime(w["date"], "%Y-%m-%d")
        if from_dt <= workout_date <= to_dt:
            results["count"] += 1
            results["duration"] += w["duration"]
            results["kcal"] += w["calories"]
            
            w_type = w["type"]
            results["type_breakdown"][w_type] = results["type_breakdown"].get(w_type, 0) + 1

    if results["count"] > 0:
        results["avg_duration"] = round(results["duration"] / results["count"], 1)

    return results
    
def delete_workout(index):
    workouts = load_workouts()
    sorted_workouts = sorted(workouts, key=lambda w: w["date"], reverse=True)

    if index < 0 or index >= len(sorted_workouts):
        return False, "Nieprawidłowy numer treningu."

    selected = sorted_workouts[index]
    workouts.remove(selected)
    save_workouts(workouts)
    return True, "Trening został pomyślnie usunięty."