import requests
from csv import reader
# with open("pandas\myfile.txt") as file:
#     contents = file.read()
#     print(contents)


# with open("pandas\myfile.txt", mode='a') as file:
#     file.write("NEW TEXT FROM PY FILE!!!")


path = "pandas\weather_data.csv"
lines = [line for line in open(path)]
sep = '/'
data = []

for line in reader(lines):
    name = ''

    if line[0] == 'Restaurant Name':
        pass
    else:
        name = line[0]

        if line[1].find(sep) != -1:

            sp_line = line[1].split('/')

            if len(sp_line) == 2:

                if sp_line[0].find(',') != -1:

                    if sp_line[0].find("Mon") != -1:

                        if sp_line[0].find("Fri") != -1:
                            data.append(
                                {"name": name, "time_open": '11:00:00', "time_close": "24:00:00", "day_start": '1', "day_end": '5'})
                            data.append(
                                {"name": name, "time_open": '11:00:00', "time_close": '24:00:00', "day_start": '6', "day_end": '6'})

                        elif sp_line[0].find("Thu") == 4:

                            if sp_line[0].find("11:30") != -1:

                                if sp_line[0].find("10 pm") != -1:
                                    data.append(
                                        {"name": name, "time_open": "11:30:00", "time_close": "22:00:00", "day_start": '1', "day_end": "4"})
                                    data.append(
                                        {"name": name, "time_open": "11:30:00", "time_close": "22:00:00", "day_start": '7', "day_end": "7"})
                                elif sp_line[0].find("9:30") != -1:
                                    data.append(
                                        {"name": name, "time_open": "11:30:00", "time_close": "21:30:00", "day_start": '1', "day_end": "4"})
                                    data.append(
                                        {"name": name, "time_open": "11:30:00", "time_close": "21:30:00", "day_start": '7', "day_end": "7"})
                                elif sp_line[0].find("9 pm") != -1:
                                    data.append(
                                        {"name": name, "time_open": "11:30:00", "time_close": "21:00:00", "day_start": '1', "day_end": "4"})
                                    data.append(
                                        {"name": name, "time_open": "11:30:00", "time_close": "21:00:00", "day_start": '7', "day_end": "7"})

                            elif sp_line[0].find("9 am") != -1:
                                data.append(
                                    {"name": name, "time_open": "09:00:00", "time_close": "22:00:00", "day_start": '1', "day_end": "4"})
                                data.append(
                                    {"name": name, "time_open": "09:00:00", "time_close": "22:00:00", "day_start": '7', "day_end": "7"})

                            elif sp_line[0].find("11 am") != -1:
                                data.append(
                                    {"name": name, "time_open": "11:00:00", "time_close": "22:00:00", "day_start": '1', "day_end": "4"})
                                data.append(
                                    {"name": name, "time_open": "11:00:00", "time_close": "22:00:00", "day_start": '7', "day_end": "7"})

                    else:
                        data.append(
                            {"name": name, "time_open": "11:30:00", "time_close": "22:00:00", "day_start": '2', "day_end": "5"})
                        data.append(
                            {"name": name, "time_open": "11:30:00", "time_close": "22:00:00", "day_start": '7', "day_end": "7"})
                else:
                    if sp_line[0].find("Sat") != -1:
                        if sp_line[0].find("11 am") != -1:
                            if sp_line[0].find("10 pm"):
                                data.append(
                                    {"name": name, "time_open": "11:00:00", "time_close": "22:00:00", "day_start": '1', "day_end": "6"})
                            elif sp_line[0].find("11 pm"):
                                data.append(
                                    {"name": name, "time_open": "11:00:00", "time_close": "23:00:00", "day_start": '1', "day_end": "6"})
                            else:
                                data.append(
                                    {"name": name, "time_open": "11:00:00", "time_close": "24:00:00", "day_start": '1', "day_end": "6"})
                        else:
                            data.append(
                                {"name": name, "time_open": "11:30:00", "time_close": "22:00:00", "day_start": '1', "day_end": "6"})

                    elif sp_line[0].find("Thu") != -1:
                        data.append(
                            {"name": name, "time_open": "11:30:00", "time_close": "22:00:00", "day_start": '1', "day_end": "4"})
                    elif sp_line[0].find("Fri") != -1:
                        if sp_line[0].find("10 am") != -1:
                            data.append(
                                {"name": name, "time_open": "10:00:00", "time_close": "21:30:00", "day_start": '1', "day_end": "5"})
                        elif sp_line[0].find("10:30") != -1:
                            data.append(
                                {"name": name, "time_open": "10:30:00", "time_close": "21:30:00", "day_start": '1', "day_end": "5"})
                        elif sp_line[0].find("11 am") != -1:
                            if sp_line[0].find('9 pm') != -1:
                                data.append(
                                    {"name": name, "time_open": "11:00:00", "time_close": "21:00:00", "day_start": '1', "day_end": "5"})
                            else:
                                data.append(
                                    {"name": name, "time_open": "11:00:00", "time_close": "22:00:00", "day_start": '1', "day_end": "5"})

                        elif sp_line[0].find("11:30") != -1:
                            data.append(
                                {"name": name, "time_open": "11:30:00", "time_close": "22:00:00", "day_start": '1', "day_end": "5"})

            elif len(sp_line) == 3:
                if name == 'Mandolin':
                    data.append(
                        {"name": name, "time_open": "11:00:00", "time_close": "22:00:00", "day_start": '1', "day_end": "4"})
                    data.append(
                        {"name": name, "time_open": "10:00:00", "time_close": "22:30:00", "day_start": '5', "day_end": "6"})
                    data.append(
                        {"name": name, "time_open": "11:00:00", "time_close": "22:00:00", "day_start": '7', "day_end": "7"})
                else:
                    data.append(
                        {"name": name, "time_open": "11:00:00", "time_close": "23:00:00", "day_start": '1', "day_end": "4"})
                    data.append(
                        {"name": name, "time_open": "11:00:00", "time_close": "24:30:00", "day_start": '5', "day_end": "6"})
                    data.append(
                        {"name": name, "time_open": "10:00:00", "time_close": "23:00:00", "day_start": '7', "day_end": "7"})

            elif len(sp_line) == 4:
                data.append(
                    {"name": name, "time_open": "17:00:00", "time_close": "24:30:00", "day_start": '1', "day_end": "3"})
                data.append(
                    {"name": name, "time_open": "17:00:00", "time_close": "01:30:00", "day_start": '4', "day_end": "5"})
                data.append(
                    {"name": name, "time_open": "15:00:00", "time_close": "01:30:00", "day_start": '6', "day_end": "6"})
                data.append(
                    {"name": name, "time_open": "15:00:00", "time_close": "23:30:00", "day_start": '7', "day_end": "7"})
        else:
            name = line[0]

            if line[1].find('Mon-Sun') != -1:

                if line[1].find('11 am') != -1:
                    if line[1].find('9:30') != -1:
                        data.append(
                            {"name": name, "time_open": "11:00:00", "time_close": "21:30:00", "day_start": '1', "day_end": "7"})
                    elif line[1].find('10 pm') != -1:
                        data.append(
                            {"name": name, "time_open": "11:00:00", "time_close": "22:00:00", "day_start": '1', "day_end": "7"})
                    elif line[1].find('10:30') != -1:
                        data.append(
                            {"name": name, "time_open": "11:00:00", "time_close": "22:30:00", "day_start": '1', "day_end": "7"})
                    elif line[1].find('11 pm') != -1:
                        data.append(
                            {"name": name, "time_open": "11:00:00", "time_close": "23:00:00", "day_start": '1', "day_end": "7"})
                    elif line[1].find('12 am') != -1:
                        data.append(
                            {"name": name, "time_open": "11:00:00", "time_close": "24:00:00", "day_start": '1', "day_end": "7"})
                    elif line[1].find('4 am') != -1:
                        data.append(
                            {"name": name, "time_open": "11:00:00", "time_close": "04:00:00", "day_start": '1', "day_end": "7"})

                elif line[1].find('11:30') != -1:
                    if line[1].find('9:30') != -1:
                        data.append(
                            {"name": name, "time_open": "11:30:00", "time_close": "21:30:00", "day_start": '1', "day_end": "7"})
                    elif line[1].find('10 pm') != -1:
                        data.append(
                            {"name": name, "time_open": "11:30:00", "time_close": "22:00:00", "day_start": '1', "day_end": "7"})
                    elif line[1].find('10:30') != -1:
                        data.append(
                            {"name": name, "time_open": "11:30:00", "time_close": "22:30:00", "day_start": '1', "day_end": "7"})

                else:
                    data.append(
                        {"name": name, "time_open": "17:00:00", "time_close": "22:00:00", "day_start": '1', "day_end": "7"})
            else:
                data.append(
                    {"name": name, "time_open": "11:00:00", "time_close": "22:00:00", "day_start": '1', "day_end": "1"})
                data.append(
                    {"name": name, "time_open": "11:00:00", "time_close": "22:00:00", "day_start": '3', "day_end": "7"})


# url = 'http://localhost:8000/api/add-hours/'
# obj = requests.post(url, data={"name": name, "time_open": "11:30:00",
#                                "time_close": "22:30:00", "day_start": '1', "day_end": "7"})
for restautant in data:
    url = 'http://localhost:8000/api/add-hours/'
    obj = requests.post(url, data=restautant)
    print(obj)
