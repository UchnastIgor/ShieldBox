# import requests
# import json

# sensor_data = {
#     'name': "Shieldbox1",
#     'value': 25.5,
# } 

# url = "http://127.0.0.1:8000/shieldbox/devices/1/sensors/"
# headers = {'Content-Type': 'application/json'}

# response = requests.post(url, data=json.dumps(sensor_data), headers=headers)

# print(response.status_code)
# import requests
# import json
# url = "http://127.0.0.1:8000/shieldbox/devices/1/sensors/"
# data = {"data": [{'name': "Shieldbox1"}, {'value':25.9}]}
# headers = {'content-type':'application/json','Cookie':'csrftoken=axXsa39e5hq8gqlTjJFHAbUWtg2FQgnSd3cxxkx9khatqgersthtSryDxtF0cVCk'}
# r = requests.post(url, data=json.dumps(data), headers=headers)
# print(r.text)
# from django.http import JsonResponse

# def my_put_view(request, resource_id):
#     if request.method == 'PUT':
#         # Logika aktualizacji zasobu o id=resource_id
#         return JsonResponse({"message": "Zasób zaktualizowany poprawnie."})

import requests
import json

url1 = "http://127.0.0.1:8000/shieldbox/devices/1/sensors/Sensor1"
url2 = "http://127.0.0.1:8000/shieldbox/devices/2/sensors/Sensor2"

data_to_send = {"name": "Sensor1", "value": 4.7}

response = requests.put(url1, data=json.dumps(data_to_send), headers={'Content-Type': 'application/json'})

print(response.status_code)
print(response.json())