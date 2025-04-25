import requests

API_KEY= "ba34458bf7d3893be6ddedf141d3f5ff"

def get_data(place, forecast_days=1):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_days = 8 * forecast_days
    filtered_data = filtered_data[:nr_days]
    return filtered_data

def get_country(place):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    country_data = data["city"]["country"]
    return country_data


if __name__ == "__main__":
    print(get_country(place="Tokyo"))