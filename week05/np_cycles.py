from urllib.request import Request, urlopen
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Parse the given url
url = "https://raw.githubusercontent.com/fmaussion/scientific_programming/master/data/innsbruck_temp.json"
req = urlopen(Request(url)).read()
# Read the data
inn_data = json.loads(req.decode("utf-8"))  # dict with year, temp, month

# %% dict to array
li = []
for i in range(3):
    li.append(list(inn_data.items())[i][1])

data = np.array(li)  # ndarray with year, temp, month. 3*492 elements

# %% mean monthly annual cycle for 1981-2010
months_n = 12
monthly_mean_1981_2010 = np.zeros(months_n)
year_diff_1981_2010 = 2010 - 1981  # to calculate average
for yr, temp, mon in data.T:
    if 1981 <= yr <= 2010:
        monthly_mean_1981_2010[int(mon - 1)] += temp / year_diff_1981_2010

# %% mean annual temperature timeseries for 1977-2017
year_diff_1977_2017 = 2017 - 1977
years = np.linspace(1977, 2017, 2018 - 1977)
mean_annual_1977_2017 = []
for year in range(1977, 2017 + 1):
    mean_annual_1977_2017.append(data[1][np.nonzero(data[0] == year)].sum() / months_n)

#  plotting


def plot_monthly_annual_cycle():
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Des",
    ]
    # months = np.linspace(0, 12, 12)
    plt.plot(months, monthly_mean_1981_2010)
    plt.ylabel("Temperature [C]")
    plt.title("Mean monthly annual cycle for 1981-2010")
    plt.grid(True)
    plt.savefig("week05/Monthly_annual_cycle_1981-2010.png")
    # plt.show()


# plot_monthly_annual_cycle()


def mean_annual_temperature_timeseries_for_1977_2017():
    plt.plot(years, mean_annual_1977_2017)
    plt.title("Mean annual temperature timeseries for 1977-2017")
    plt.ylabel("Temperature [C]")
    plt.xlabel("Year")
    plt.grid(True)
    plt.savefig("week05/mean_annual_temperature_timeseries_for_1977-2017.png")
    plt.show()


# mean_annual_temperature_timeseries_for_1977_2017()


#%%Compute the linear trend (using scipy.stats.linregress)
# of the average annual temperature over 1977-2017.

# slope, intercept, r_value, p_value, stderr = linregress(years, mean_annual_1977_2017)
slope, intercept, r_value, p_value, stderr = linregress(
    np.arange(len(years)), mean_annual_1977_2017
)
linreg = intercept + slope * years - years[0] * slope
# plt.plot(years, linreg)


def plot_mean_with_linreg_1977_2010():
    plt.plot(years, mean_annual_1977_2017, label="Data")
    plt.plot(
        years,
        linreg,
        label=f"Linreg: T(year) = {round(intercept, 2)} + year * {round(slope, 3)} ",
    )
    plt.legend()
    plt.show()


plot_mean_with_linreg_1977_2010()

#%% Repeat linreg with winter (DJF) and summer (JJA) trends.
djf = np.array([1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
jja = np.array([0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0])


def specific_months_linreg(months):
    months_mean_annual_1977_2017 = []
    for year in range(1977, 2017 + 1):
        months_mean_annual_1977_2017.append(
            np.array([data[1][np.nonzero(data[0] == year)] * months]).sum()
            / months.sum()
        )
    slope, intercept, r_value, p_value, stderr = linregress(
        np.arange(len(years)), months_mean_annual_1977_2017
    )
    linreg = intercept + slope * years - years[0] * slope
    return months_mean_annual_1977_2017, linreg


djf_data, djf_linreg = specific_months_linreg(djf)
jja_data, jja_linreg = specific_months_linreg(jja)


#%% plotting specific months
plt.plot(years, djf_data, label="Data DJF")
plt.plot(
    years,
    djf_linreg,
    label=f"Linreg DJF",
)
plt.plot(years, np.array(jja_data) - 15, label="Data JJA - 15C")
plt.plot(
    years,
    np.array(jja_linreg) - 15,
    label=f"Linreg JJA - 15C",
)
plt.title("Mean annual temperature timeseries for DJF and JJA 1977-2017")
plt.xlabel("Year")
plt.ylabel("Temperature [C]")
plt.legend()
plt.grid(True)
plt.savefig("week05/mean_annual_temperature_timeseries_for_DJF_and_JJA_1977-2017.png")
plt.show()
