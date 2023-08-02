import requests
from get_weather_data import get_weather_data
from get_option_from_user import get_option_from_user
from get_data_by_date import get_data_by_date
from print_temperature import print_temperature
from print_wind_speed import print_wind_speed
from print_pressure import print_pressure

if __name__ == "__main__":
    weather_data = get_weather_data()
    while True:
        option = get_option_from_user()
        if option == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            data = get_data_by_date(weather_data, date)
            print_temperature(data)
        elif option == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            data = get_data_by_date(weather_data, date)
            print_wind_speed(data)
        elif option == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            data = get_data_by_date(weather_data, date)
            print_pressure(data)
        elif option == "0":
            break
        else:
            print("Invalid option. Please try again.")
