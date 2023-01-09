from datetime import datetime


def get_days_from_today(date):
    s_list = date.split("-")
    data_new = datetime(year=int(s_list[0]), month=int(
        s_list[1]), day=int(s_list[2]))
    data_new_d = data_new.date()
    cur_data = datetime.now()
    cur_data_d = cur_data.date()
    difference = cur_data_d - data_new_d
    return difference.days


print(get_days_from_today('2021-10-09'))
