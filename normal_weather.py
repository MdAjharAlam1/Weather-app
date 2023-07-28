import requests
city = input("Enetr city Name : -> ")
data1 = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=3aca17ab5e4b932824a61c6def2479c3").json()
print(" The Temprature of",city,"is",str(int(data1["main"]["temp"]-273.15))+"°C")