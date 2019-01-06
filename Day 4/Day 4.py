import re
import pandas as pd
from collections import defaultdict
guard_logs = open("input.txt").read().split("\n")
guard_dict = {}
for log in guard_logs[:-1]:
    date = str(re.search("\[(.*)\]", log).group(1))
    event = str(re.search("\] (.*)", log).group(1))
    guard_dict[date] = event
guard_logs = pd.Series(guard_dict).sort_index()
guard_naps={}
counter=0

for i in guard_logs.index:
    log = guard_logs[i]

    if "Guard" in log:
        guard_id = int(re.search("#(.*) b",log).group(1))
        if not guard_id in guard_naps:
            guard_naps[guard_id] = defaultdict(int)
        # print(log)
        # print(guard_id)
    if "falls asleep"==log:
        # print(counter)
        start_nap = int(re.search(":(.*)",guard_logs.index[counter]).group(1))
    if "wakes up"==log:
        stop_nap = int(re.search(":(.*)",guard_logs.index[counter]).group(1))
        guard_naps[guard_id]['Total minutes'] += stop_nap-start_nap
        for j in range(start_nap,stop_nap):
            guard_naps[guard_id][j] += 1
    counter+=1
# print(guard_naps)

most_minutes_slept = 0
most_sleepy_guard = 0
for guard in guard_naps:
    if guard_naps[guard]['Total minutes'] > most_minutes_slept:
        most_minutes_slept = guard_naps[guard]['Total minutes']
        most_sleepy_guard = guard
most_sleepy_minute = 0
most_sleep = 0
# Part 1
for minute in guard_naps[most_sleepy_guard]:
    if minute!='Total minutes':
        if guard_naps[most_sleepy_guard][minute]>most_sleep:
            most_sleepy_minute = minute
            most_sleep = guard_naps[most_sleepy_guard][minute]
print("Answer",most_sleepy_guard*most_sleepy_minute)

# Part 2
most_frequently_asleep_minute = 0
highest_sleep_frequency = 0
most_frequently_asleep_guard = 0
for guard in guard_naps:
    for minute in guard_naps[guard]:
        if minute != 'Total minutes':
            if guard_naps[guard][minute]>highest_sleep_frequency:
                most_frequently_asleep_minute = minute
                highest_sleep_frequency = guard_naps[guard][minute]
                most_frequently_asleep_guard = guard
print("Answer",most_frequently_asleep_guard*most_frequently_asleep_minute)

