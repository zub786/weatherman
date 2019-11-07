import sys
import os
from datetime import datetime

if __name__ == "__main__":
    date = sys.argv[1]
    # filesPath = sys.argv[2] + "/" + "lahore_weather_1996_Dec.txt"
    dataFilesList = [x for x in os.listdir(sys.argv[2])]
    filesOfTheYear = [fileName for fileName in dataFilesList if date in fileName]
    MaxTemprature = []
    LowestTemprature = []
    MostHumid = []
    Dates = []

    for filePath in filesOfTheYear:
        with open(sys.argv[2] + "/" + filePath, 'r') as fp:
            line = fp.readline()
            cnt = 1
            while line:
                # print("Line {}: {}".format(cnt, line.strip()))
                if cnt >= 3:
                    weatherDetail = line.split(',')
                    if len(weatherDetail) > 20:
                        MaxTemprature.append(0 if weatherDetail[1] == '' else int(weatherDetail[1]))
                        LowestTemprature.append(0 if weatherDetail[3] == '' else int(weatherDetail[3]))
                        MostHumid.append(0 if weatherDetail[7] == '' else int(weatherDetail[7]))
                        Dates.append(weatherDetail[0])
                        # print("{} | {} | {} | {}".format(weatherDetail[0],weatherDetail[1],weatherDetail[3],weatherDetail[7]))

                line = fp.readline()
                cnt += 1

    print("\t\t\t\t*** RESULTS OF THE YEAR ***")
    maxTempIndex = MaxTemprature.index(max(MaxTemprature))
    print("Highest: {}C on {}".format(MaxTemprature[maxTempIndex], Dates[maxTempIndex]))

    lowestTempIndex = LowestTemprature.index(max(LowestTemprature))
    print("Lowest: {}C on {}".format(LowestTemprature[lowestTempIndex], Dates[lowestTempIndex]))

    mostHumidIndex = MostHumid.index(max(MostHumid))
    print("Humit: {}% on {}".format(MostHumid[mostHumidIndex], datetime.strptime(Dates[mostHumidIndex], '%b %d %Y')))
