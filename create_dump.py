import googlemaps # for travel times
from datetime import datetime, tzinfo # so we can specify departure time
import json # google maps returns a json

gmaps = googlemaps.Client(key=open("params/API_KEY").read())
addresses = open(open("params/FILE_PATH").read())
lines = addresses.read().split("\n")
print(lines)
dumps = list()
output = open("distancedump.txt", "w")

count = 0
max = 0
min = 999999999
maxAddr = ""
minAddr = ""
for addr in lines:
    try:
        directions_result = gmaps.directions("The Overlake School",
                                        addr,
                                        mode="driving",
                                        departure_time=datetime(2019, 9, 2, hour=15, minute=30))
        #all output is in miles
        distance = directions_result[0]['legs'][0]['distance']['text']
        distance = distance[:-3] # remove ' mi' from end
        distance = distance.replace(',', '')
        num = float(distance)
        print(addr + ": " + str(num))
        
        if (num > max):
            max = num
            maxAddr = addr
        if (num < min):
            min = num
            minAddr = addr
        distance += "\n"
        output.write(distance)
        if (count % 10 == 0):
            print(count)
        count += 1
    except:
        print("Problem with " + addr)

print("Max: " + maxAddr + " with distance " + str(max))
print("Min: " + minAddr + " with distance " + str(min))