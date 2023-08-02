def print_wind_speed(data):
    if data:
        print(f"Wind Speed on {data['dt_txt']}: {data['wind']['speed']} m/s")
    else:
        print("No data found for the provided date.")
