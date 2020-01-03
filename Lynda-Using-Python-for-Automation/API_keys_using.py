# How to use keys to raise API
# Example of using https://openweathermap.org/api
# Usefull resource: https://rapidapi.com
import requests

baseUrl = 'https://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID':'ee8618bc4f45acffacdfced838d5cfcb', 'q':'Prague,CZ'}

response = requests.get(baseUrl, params=parameters)
print(response.content)

