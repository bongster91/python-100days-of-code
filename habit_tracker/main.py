import requests
from datetime import datetime

USERNAME = 'bongster'
TOKEN = 'thisisarandomtokenforpixela'
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = 'graph1'
TOTAL_ENDPOINT = f'{GRAPH_ENDPOINT}/{GRAPH_ID}'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)

today = datetime.now()
graph_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": '10'
}

# response = requests.post(url=TOTAL_ENDPOINT, json=graph_data, headers=headers)

PUT_ENDPOINT = f"{TOTAL_ENDPOINT}/{today.strftime("%Y%m%d")}"
response = requests.put(url=PUT_ENDPOINT, json=graph_data, headers=headers)
print(response.text)

