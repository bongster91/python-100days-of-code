import requests
from datetime import datetime

APP_ID = '57f36225'
API_KEY = '3510ee8952ceda4207db8135cbef9861'
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = 'female'
WEIGHT_KG = 100
HEIGHT_CM = 150
AGE = 30

exercise_input = input("Tell me which exercises you did: ")

exercise_data = {
    "query":exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_data, headers=headers)
exercise_result = exercise_response.json()

SHEETY_ENDPOINT = 'https://api.sheety.co/0c6b9b242195b7fa63de8acefcabc6ea/myWorkouts/workouts'

workout_response = requests.get(url=SHEETY_ENDPOINT)

today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

for exercise in exercise_result['exercises']:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise['name'].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
    header = {
        "Authorization": ''
    }
    
    post_workout = requests.post(url=SHEETY_ENDPOINT, json=sheet_input, headers=header)
    print(post_workout.text)