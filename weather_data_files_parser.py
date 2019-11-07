import sys
import os
from models import Weather
import calendar

def parse_files(date, data_files_list, root_path, info_type):
    weather_years = []
    if info_type == '-e':
        files = [file_name for file_name in data_files_list if date in file_name]
    elif info_type == '-a':
        files = [file_name for file_name in data_files_list if calendar.month_name[int(date.split('/')[1])][0:3] in file_name]
    for file_path in files:
        with open(root_path+ "/" + file_path, 'r') as fp:
            line = fp.readline()
            cnt = 1
            while line:
                if cnt >= 3 and '<!--' not in line:
                    weatherDetail = line.split(',')
                    weather = Weather()
                    weather.max_temprature = 0 if weatherDetail[1] == '' else int(weatherDetail[1])
                    weather.lowest_temprature = 0 if weatherDetail[3] == '' else int(weatherDetail[3])
                    weather.most_humid = 0 if weatherDetail[7] == '' else int(weatherDetail[7])
                    weather.date = weatherDetail[0]
                    weather_years.append(weather)
                line = fp.readline()
                cnt += 1
    return weather_years
