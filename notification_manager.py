from twilio.rest import Client

account_sid = 'AC6cfe0cdea4775d8cadfd4e2023228325'
auth_token = '9950f4656985fc96fdac23b7ea65e520'


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, FlightData):
        self.msg = f"Low price alert! Only £{FlightData.price} " \
                   f"to fly from {FlightData.origin_city}-{FlightData.origin_airport} to " \
                   f"{FlightData.destination_city}-{FlightData.destination_airport},from " \
                   f"{FlightData.out_date} to {FlightData.return_date}"
        self.to_list = "+918901116612"

    def send_massage(self):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=self.msg,
            from_='+18059024520',
            to=self.to_list,
        )
        print(message.status)
