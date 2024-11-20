import requests
import datetime as dt
from requests.auth import HTTPBasicAuth


APP_ID = ''
API_KEY = ''


GENDER = 'gender'
WEIGHT_KG = 'yourweight'
HEIGHT_CM = 'height in cm'
AGE = 'age'

endpoints = 'https://trackapi.nutritionix.com/v2/natural/exercise'


exerise_type = input("Please enter the type of exercises you did: ")

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}
parameter = {
    'query': exerise_type,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

repsonse = requests.post(url=endpoints, json=parameter, headers=headers)
result = repsonse.json()



worksheet_endpoint = 'Youworkendpoints'


today_date = dt.datetime.now().strftime('%d/%m/%Y')
now_time = dt.datetime.now().strftime('%X')

basic = HTTPBasicAuth('yourownUser', 'yourownPWD')
    
header_authorization = {
    'Authorization': 'Basic yourown'
}


for exercise in result['exercises']:

    body = {
        'workout':
            {
                'date': today_date,
                'time': now_time,
                'exercise': exercise['user_input'].title(),
                'duration': exercise['duration_min'],
                'calories': exercise['nf_calories']
            }
    }
    response_worksheet = requests.post(url=worksheet_endpoint, json=body, headers=header_authorization, auth=basic)