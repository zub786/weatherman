import sys
import os
from os import system
from datetime import datetime
import calendar
import weather_data_files_parser
import statistics


if __name__ == "__main__":
    info_type = sys.argv[1]
    date = sys.argv[2]
    data_files_list = [x for x in os.listdir(sys.argv[3])]

    if info_type == '-e':


        # Passing file names to parse engine to get list of weather
        list_of_weather_year = weather_data_files_parser.parse_files(date, data_files_list, sys.argv[3], info_type)

        max_temp = max([mt.max_temprature for mt in list_of_weather_year])
        lowest_temp = max(lt.lowest_temprature for lt in list_of_weather_year)
        most_humid = max(mh.most_humid for mh in list_of_weather_year)

        system('clear')
        print("\t\t\t\t*** RESULTS OF THE YEAR ***")
        max_temp_date = [mt.date for mt in list_of_weather_year if mt.max_temprature is max_temp][0].split('-')
        print("\t\t\t\tHighest: {}C on {} {}".format(max_temp, calendar.month_name[int(max_temp_date[1])], max_temp_date[2]))
        lowest_temp_date = [ltd.date for ltd in list_of_weather_year if ltd.lowest_temprature is lowest_temp][0].split('-')
        print("\t\t\t\tLowest: {}C on {} {}".format(lowest_temp, calendar.month_name[int(lowest_temp_date[1])], lowest_temp_date[2]))
        most_humid_date = [mh.date for mh in list_of_weather_year if mh.most_humid is most_humid][0].split('-')
        print("\t\t\t\tHumid: {}% on {} {}".format(most_humid, calendar.month_name[int(most_humid_date[1])], most_humid_date[2]))
    elif info_type == '-a':

        files_of_the_month = weather_data_files_parser.parse_files(date, data_files_list, sys.argv[3], info_type)

        system('clear')
        print("\t\t\t\t*** RESULTS OF THE MONTH ***")
        print("\t\t\t\tHighest Average: {}C".format(int(statistics.mean([mt.max_temprature for mt in files_of_the_month]))))
        print("\t\t\t\tLowest Average: {}C".format(int(statistics.mean(lt.lowest_temprature for lt in files_of_the_month))))
        print("\t\t\t\tAverage Humidity: {}%".format(int(statistics.mean(mh.most_humid for mh in files_of_the_month))))
