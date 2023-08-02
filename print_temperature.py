def print_temperature(data):
    if data:
        print(f"Temperature on {data['dt_txt']}: {data['main']['temp']} °K")
    else:
        print("No data found for the provided date.")
