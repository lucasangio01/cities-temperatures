from opencage.geocoder import OpenCageGeocode
from countryinfo import CountryInfo
import pandas as pd


# The following class contains the imported data and data that I used frequently in other functions.

class Data:
    tempByCity = pd.read_csv("C:/Users/sangi/Downloads/GlobalLandTemperaturesByCity.csv/GlobalLandTemperaturesByCity.csv").dropna().reset_index(drop=True)
    tempByMajorCity = pd.read_csv("https://raw.githubusercontent.com/lucasangio01/cities-temperatures/main/datasets/GlobalLandTemperaturesByMajorCity.csv").dropna().reset_index(drop=True)
    majorCities = pd.read_csv("https://raw.githubusercontent.com/lucasangio01/cities-temperatures/main/datasets/majorCities.csv", index_col=0)
    cities = pd.read_csv("https://raw.githubusercontent.com/lucasangio01/cities-temperatures/main/datasets/cities.csv", index_col=0)
    cities_old = pd.read_csv("https://raw.githubusercontent.com/lucasangio01/cities-temperatures/main/datasets/cities_old.csv", index_col=0, on_bad_lines="skip")
    months = {"01": 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July',
              '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}

