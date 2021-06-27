from numpy import short
import pandas as pd
from pandas.core.indexes import period
import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=34.09976000000006&lon=-118.33197499999994#.YNiKhegzZEY')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id="seven-day-forecast-body")
items = week.find_all(class_='tombstone-container')

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [
    item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

weather_stuff = pd.DataFrame(
    {
        'period': period_names,
        'short_descriptions': short_descriptions,
        'temperatures': temperatures,
    }
)

print(weather_stuff)

weather_stuff.to_csv('result.csv')
