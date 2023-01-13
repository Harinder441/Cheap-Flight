from twilio.rest import Client

account_sid = YOUR_TWILLIO_SID
auth_token = YOUR_AUTH_TOKEN


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, FlightData):
        self.msg = f"Low price alert! Only £{FlightData.price} " \
                   f"to fly from {FlightData.origin_city}-{FlightData.origin_airport} to " \
                   f"{FlightData.destination_city}-{FlightData.destination_airport},from " \
                   f"{FlightData.out_date} to {FlightData.return_date}"
        self.to_list = RECIEVERS_MOBILE_NUMBER

    def send_massage(self):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=self.msg,
            from_= YOUR_TWILIO_MOBILE_NUMBER,
            to=self.to_list,
        )
        print(message.status)
