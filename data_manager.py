from pprint import pprint
import requests
# get your Api Endpoint from sheety 
SHEETY_PRICES_ENDPOINT = YOUR-API

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """will get the list of destinations from your list (google sheet) """
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
  
        # pprint(data)
        return self.destination_data


    def update_destination_codes(self):
        """genearate IATA codes for your destination and update in sheet"""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
        


if __name__ == "__main__":
    pass
