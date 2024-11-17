import requests
import random

USERNAME = 'jason31'
TOKEN = 'yourownapitoken'



pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': 'yourownapitoken',
    'username': 'jason31',
    'agreeTermsOfService' : 'yes',
    'notMinor': 'yes'
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoints = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': 'graph1',
    'name': 'Cycling Graph',
    'unit': 'Hour',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

response = requests.post(url= graph_endpoints, json=graph_config, headers=headers)
print(response.text)

#POST records the quantity of the specificed date as a Pixel.
graph_endpoints_test = f'{pixela_endpoint}/{USERNAME}/graphs/graph1'


#For 30 Days commit 
for days in range(1, 31):
    if 0 <= days <= 9:
        days = '0' + str(days)
    graph_pixel = {
        'date': f'202411{days}',
        'quantity': f'{random.randint(1,20)}'
    }
    response = requests.post(url=graph_endpoints_test, json=graph_pixel, headers=headers)


#Update pixel using PUT
graph_pixel_update = {
    'date': f'20241115',
    'quantity': '2'
}
graph_endpoints_put = f'{pixela_endpoint}/{USERNAME}/graphs/graph1/20241115'
response = requests.put(url=graph_endpoints_put, json=graph_pixel_update, headers=headers)
print(response.text)


#Delete pixel using DELETE
graph_endpoints_del = f'{pixela_endpoint}/{USERNAME}/graphs/graph1/20241116'
response = requests.delete(url=graph_endpoints_del, headers=headers)
print(response.text)