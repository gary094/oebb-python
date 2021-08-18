import requests
import json
from datetime import datetime


def auth():
    auth_response = json.loads(requests.get("https://tickets.oebb.at/api/domain/v4/init").text)
    headers = {"AccessToken": auth_response["accessToken"], "sessionId": auth_response["sessionId"]}
    return headers

#def connections(orig, dest, date=datetime.now().strftime("%Y-%m-%dT%H:%M:00.000")):


if __name__ == "__main__":
    origin = {"type": "station", "id": "1292103", "name": "Leopoldau (Wien) Bahnhst"}
    destination = {"type": "station", "id": "1291201", "name": "Wien Meidling Bahnhof (U)"}

    travel_actions_data = {"from": {"number": "1291201", "name": "Wien Meidling Bahnhof (U)"}, "to": {"number": "1291201", "name": "Wien Meidling Bahnhof (U)"}, "datetime": "2021-08-15T11:28:00.028Z", "filter": {"productTypes": "[]", "history": "true", "maxEntries": "5", "channel": "inet"}}

    headers = auth()
    r = requests.post("https://tickets-mobile.oebb.at/api/offer/v2/travelActions", headers=headers, data=travel_actions_data)

    print(r.text)

