import os
import datetime
import math
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm, trange
from time import sleep

#Nested Dictionary
eventIDs = {'1102': {'count': 0}, '4611': {'count': 0}, '4624': {'count': 0}, '4634': {'count': 0},
'4648': {'count': 0}, '4661': {'count': 0}, '4662': {'count': 0}, '4663': {'count': 0}, '4672': {'count':
0}, '4673': {'count': 0}, '4688': {'count': 0}, '4698': {'count': 0}, '4699': {'count': 0}, '4702':
{'count': 0}, '4703': {'count': 0}, '4719': {'count': 0}, '4732': {'count': 0}, '4738': {'count': 0},
'4742': {'count': 0}, '4776': {'count': 0}, '4798': {'count': 0}, '4799': {'count': 0}, '4985': {'count':
0}, '5136': {'count': 0}, '5140': {'count': 0}, '5142': {'count': 0}, '5156': {'count': 0}, '5158':
{'count': 0}}

#L20:Opens file in same folder, L23:For each line in file use nested statement, L27:Match eventID to dict key.
#L27:If statement and key is in line, L28:Iterate dict count(value) +1, L29:Break loop when key is found in line and execute at start of loop.
file = open('analysis_log_02_Jan_2020_13_07_41.txt', '+r')
pbar = tqdm(total=18946)
pbar.set_description(f'Processing Event File')
for line in file:
    pbar.update(1)
    sleep(0.0)
    for event in eventIDs:
        if "MATCHED Event ID: " + event in line:
            eventIDs[event]["count"] = eventIDs[event]["count"] + 1
            break

#Console Printout
print("SEIM in Python by Indy")

#L35: Converts dict keys to y axis, L36: Converts dict values to y axis.
ids = list(eventIDs.keys())
eventCounts = []

#Iterate the dictionary to get the event count number for each event.
for key in eventIDs: 
    eventCounts.append(eventIDs[key]["count"]) #adding the event count to the correspondent Event ID
fig = plt.figure(figsize=(10, 5))
 
#Creating bar plot, L44: ids = argument is list with y axis values, eventCounts is list with x axis values.
plt.barh(ids, eventCounts, color='maroon') 
plt.xlabel("Event Count")
plt.ylabel("Event IDs")
plt.title("Event Data")
plt.show()

#Function to add time & date to log file.
def timeStamp(fname, fmt='{fname}_%Y-%m-%d-%H-%M-%S.txt'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)

#Create log file with incorporated time stamp function.
with open(timeStamp("visdata_log"),'w+') as f:  
    for key, value in eventIDs.items():
        f.write("\nEvent ID: {}".format(key))
        f.write("\nEvent Count: {}".format(value["count"]))
        f.write('\n''')