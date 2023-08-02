def print_pressure(data):
    if data:
        print(f"Pressure on {data['dt_txt']}: {data['main']['pressure']} hPa")
    else:
        print("No data found for the provided date.")
