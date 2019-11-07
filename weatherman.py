import sys
import os
from os import system
import weather_data_files_processor
import argparse

# Parssing arguments
parser = argparse.ArgumentParser(description="""Generate weather
 report""")
parser.add_argument("path", type=str, help="""to get the path of
 weather directory""")
parser.add_argument("-e", "--e", help="""Flag to generate
yearly report""", type=str)
parser.add_argument("-a", "--a", help="""Flag to generate
monthly report""", type=str)
parser.add_argument("-c", "--c", help="", type=str)
args = parser.parse_args()

if args.e:
    date = args.e
    info_type = '-e'
elif args.a:
    date = args.a
    info_type = '-a'
elif args.c:
    date = args.c
    info_type = '-c'

data_files_list = [x for x in os.listdir(args.path)]
# Passing files to parse engine to get list of weather
parsed_list = weather_data_files_processor.parse_files(date,
 data_files_list, args.path, info_type)
# Passing files to parse engine to get list of weather
# by passing filter data list and information type
weather_data_files_processor.generate_report(parsed_list, info_type)
