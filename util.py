import time


def conver_UNIX_to_datetime(given_row, time_index):
    updated_dict = {}
    # print(int(row[time_index]))
    # print(time.localtime(int(row[time_index])))
    print("start" + given_row[time_index] + "end")
    date_year_str = given_row[time_index]
    print(date_year_str.isdigit())
    print(date_year_str)
    date_time_converted = int(date_year_str)
    date_and_time = time.strftime("%D %H:%M", time.localtime(date_time_converted))
    for key, value in given_row.items():
        if key != time_index:
            updated_dict[key] = value
        else:
            updated_dict[key] = date_and_time

    return updated_dict
