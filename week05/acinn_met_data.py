from urllib.request import Request, urlopen
import json
import numpy as np
from datetime import datetime, timedelta

ndays = 7
statname = "innsbruck"

url = "https://acinn-data.uibk.ac.at/{}/{}".format(statname, ndays)
# Parse the given url
req = urlopen(Request(url)).read()
# Read the data
data = json.loads(req.decode("utf-8"))
data["time"] = [
    datetime(1970, 1, 1) + timedelta(milliseconds=ds) for ds in data["datumsec"]
]


#%%
ws = data["ff"]
wd = data["dd"]
time = data["time"]

d = dict(statname=statname, ndays=ndays)

awm = np.argmax(ws)
d["wsmax"] = ws[awm]
d["wsmax_time"] = time[awm]

cumsum = np.cumsum(ws)
wsh = (cumsum[6:] - cumsum[:-6]) / 6

awm = np.argmax(wsh)
d["wsmaxh"] = ws[awm]
d["wsmaxh_time"] = time[awm]

wind_classes = ["N", "NW", "W", "SW", "S", "SE", "E", "NE"]
wind_bins = np.concatenate([[0], np.arange(8) * 45 + 22.5, [360]])

(
    n_events,
    _,
) = np.histogram(wd, wind_bins)

n_events[0] += n_events[-1]
n_events = n_events[:-1]
events_perc = n_events / np.sum(n_events) * 100

aso = np.argsort(events_perc)
classes = [(wind_classes[i], events_perc[i]) for i in aso[::-1]]

d["wd1"] = classes[0][0]
d["ws1"] = classes[0][1]
d["wd2"] = classes[1][0]
d["ws2"] = classes[1][1]
d["wd3"] = classes[-1][0]
d["ws3"] = classes[-1][1]


s = (
    "At station {statname}, over the last {ndays} days, the dominant "
    "wind direction was {wd1} ({ws1:.0f}% of the time). The second most "
    "dominant wind direction was {wd2} ({ws2:.0f}% of the time), the "
    "least dominant wind direction was {wd3} ({ws3:.0f}% of the time). "
    "The maximum wind speed was {wsmax:.1f} m/s ({wsmax_time}), while "
    "the strongest wind speed averaged over an hour was {wsmaxh:.1f} m/s "
    "({wsmaxh_time})."
)
print(s.format(**d))


# all below is my old bs
# n_elements = 8
# li = []
# for i in range(n_elements):
#     li.append(list(data.items())[i][1])
#
# data_arr = np.array(li)  # ndarray with year, temp, month. 3*492 elements
# #%%
# import matplotlib.pyplot as plt
#
#
# plt.plot(data["time"], data["dd"], ".")
# plt.ylabel("Wind direction (°)")
# plt.title("Wind direction at Innsbruck")
#
#
# #%%
# wind_sector = 360 / 8
# winds = np.array([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5, 360.0])
# # N, NW, W, SW, S, SE, E, NE, N
# # n = data_arr * [data_arr[1] < winds[0]] * [data_arr[1] > winds[7]]
#
# sectors = np.histogram(data_arr[1], winds)
# #
#
#
#
#
#
#
#
#
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
#
# #%%
#
#
# def split_in_sector(lower, arr=data_arr):
#     upper = lower + wind_sector
#     sector = arr * [arr[1] >= lower] * [arr[1] <= upper]
#     sector[1][sector[1] == 0.0] = np.nan  # replace 0s with nan
#     return sector
#
#
# def sector_n(arr=data_arr):
#     lower = 22.5
#     upper = 337.5
#     sector_l = arr * [arr[1] <= lower]
#     sector_u = arr * [arr[1] >= upper]
#     sector = sector_u + sector_l
#     return sector
#
#
# data_arr * [data_arr[1] <= 22.5]
#
# # n = split_in_sector(0, 22.5)
# # n = n + split_in_sector(337.5, 360)
# nw = split_in_sector(winds[0])
# w = split_in_sector(winds[1])
# sw = split_in_sector(winds[2])
#
# plt.plot(data["time"], nw[1], ".")
# plt.plot(data["time"], w[1], ".")
# plt.plot(data["time"], sw[1], ".")
# plt.show()
#
# # nw = data_arr * [data_arr[1] > winds[1]] * [data_arr[1] < winds[2]]
# # nw[1][nw[1] == 0.0] = np.nan
# #
# # plt.plot(data["time"], nw[1], ".")
# # plt.show()
