from parser import Parse
import sys
import os
from os import system
from datetime import datetime
import calendar
import statistics

def parse_files(date, data_files_list, root_path, info_type):
    weather_years = Parse(date, data_files_list, root_path, info_type)
    return weather_years.data


def generate_report(parsed_list, info_type):
    if info_type == '-e':
        max_temp = max([mt.max_temprature for mt in parsed_list])
        lowest_temp = max(lt.lowest_temprature for lt in parsed_list)
        most_humid = max(mh.most_humid for mh in parsed_list)

        system('clear')
        print("\t\t\t\t*** RESULTS OF THE YEAR ***")
        max_temp_date = [mt.date for mt in parsed_list if mt.max_temprature is max_temp][0].split('-')
        print("\t\t\t\tHighest: {}C on {} {}".format(max_temp, calendar.month_name[int(max_temp_date[1])], max_temp_date[2]))
        lowest_temp_date = [ltd.date for ltd in parsed_list if ltd.lowest_temprature is lowest_temp][0].split('-')
        print("\t\t\t\tLowest: {}C on {} {}".format(lowest_temp, calendar.month_name[int(lowest_temp_date[1])], lowest_temp_date[2]))
        most_humid_date = [mh.date for mh in parsed_list if mh.most_humid is most_humid][0].split('-')
        print("\t\t\t\tHumid: {}% on {} {}".format(most_humid, calendar.month_name[int(most_humid_date[1])], most_humid_date[2]))
    elif info_type == '-a':
        system('clear')
        print("\t\t\t\t*** RESULTS OF THE MONTH ***")
        print("\t\t\t\tHighest Average: {}C".format(int(statistics.mean([mt.max_temprature for mt in parsed_list]))))
        print("\t\t\t\tLowest Average: {}C".format(int(statistics.mean(lt.lowest_temprature for lt in parsed_list))))
        print("\t\t\t\tAverage Humidity: {}%".format(int(statistics.mean(mh.most_humid for mh in parsed_list))))
