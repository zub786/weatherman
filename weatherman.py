import sys
import os
from os import system
import weather_data_files_processor
import argparse


if __name__ == "__main__":

    # Parssing arguments
    parser = argparse.ArgumentParser(description="""Generates the
                                        Lahore Weather Reports""")
    parser.add_argument('info_type', type=str, help='Weather Report Type')
    parser.add_argument('date', type=str, help='Date Of Weather Report')
    parser.add_argument('rootpath', type=str, help='Date Of Weather Report')
    args = parser.parse_args()
    data_files_list = [x for x in os.listdir(args.rootpath)]
    # Passing files to parse engine to get list of weather
    parsed_list = weather_data_files_processor.parse_files(args.date, data_files_list, args.rootpath, args.info_type)
    # Passing files to parse engine to get list of weather by passing filter data list and information type
    weather_data_files_processor.generate_report(parsed_list, info_type)
