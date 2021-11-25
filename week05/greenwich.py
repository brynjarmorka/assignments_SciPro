#%%
from urllib.request import Request, urlopen
from io import BytesIO
import json
import numpy as np
import matplotlib.pyplot as plt


# Parse the given url
url = "https://github.com/fmaussion/scientific_programming/raw/master/data/monthly_temp.npz"
req = urlopen(Request(url)).read()
with np.load(BytesIO(req)) as data:
    temp = data["temp"]
    lon = data["lon"]
    lat = data["lat"]
#%%
p = np.nonzero(lon > 180)
new_lon = np.roll(lon, -p[0][0])
new_temp = np.roll(temp, -p[0][0], axis=1)
new_lon = np.where(new_lon > 180, new_lon - 360, new_lon)


#%% plot

dx = (new_lon[1] - new_lon[0]) / 2
dy = (lat[1] - lat[0]) / 2
extent = [new_lon[0] - dx, new_lon[-1] + dx, lat[0] - dy, lat[-1] + dy]

plt.figure(figsize=(10, 4))
plt.imshow(new_temp, cmap="RdBu_r", extent=extent, vmin=-30, vmax=30)
plt.show()
