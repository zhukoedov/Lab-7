import requests


def openworldmap():
    owm_api_key='7e2aa03196014d5b5280b53abac6a6a5'
    city_name='Ulan-Ude'
    city_id=2014407
    
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                    params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': owm_api_key})
        data = res.json()
        print("conditions:", data['weather'][0]['description'])
        print("temp:", data['main']['temp'])
        print("humidity:", data['main']['humidity'])
        print("pressure:", data['main']['pressure'])
    except Exception as e:
        print("Exception (weather):", e)
        pass
    
def holidayapi():
    hol_api_key='6b791603-f4ec-4e35-8991-44fe01832641'
    year=2024
    
    try:
        res = requests.get("https://holidayapi.com/v1/holidays?pretty&key=6b791603-f4ec-4e35-8991-44fe01832641&country=RU&year=2024")
        data = res.json()
        # print(data)
        # print("######### NEW STRING #########")
        for holiday in data['holidays']:
            print(holiday['name'])
            print("  Date:", holiday['date'],"\n  Weekday:",holiday['weekday']['date']['name'], "\n  Country:", holiday['country'])
            if holiday['public']:
                print("  Public")
            else:
                print("  Non-Public")
        
    except Exception as e:
        print("exception(holidays):", e)
        pass

if __name__ == "__main__":
    openworldmap()
    print("#### Part 2 ####")
    holidayapi()
    