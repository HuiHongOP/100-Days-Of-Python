import os
import requests
from requests.auth import HTTPBasicAuth


SHEETY_END_POINT = 'https://api.sheety.co/5f89d6df22508471eb8d84250f306a0f/flightDeals/prices'


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = '**********'
        self._password = 'A**'
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self._authorization_token = '***********'
        self.destination_data = {}
    
    def get_destination_data(self):
        response = requests.get(url=SHEETY_END_POINT)
        data = response.json()
        self.destination_data = data['prices']
        print(data)
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                'price':{
                    'iataCode': city['iataCode']
                }
            }
            header_authorization = {
            'Authorization': f'Basic {self._authorization_token}'
}
            response = requests.put(url=f"{SHEETY_END_POINT}/{city['id']}", 
                                    json=new_data, 
                                    headers= header_authorization,
                                    auth=self._authorization)
            print(response.text)
            