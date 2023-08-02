def get_data_by_date(data_list, date):
    for data in data_list:
        if data["dt_txt"].startswith(date):
            return data
    return None
