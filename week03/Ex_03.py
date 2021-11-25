# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:54:00 2021

@author: Paula
"""

import urllib.request
import math
import os
import sys
import pathlib


def coordinates2tilepath(lon, lat):
    # Check if input for longitutde and latitude is valid

    lon_valid = range(-180, 181)
    lat_valid = range(-60, 61)

    if lon not in lon_valid or lat not in lat_valid:
        raise TypeError("The coordinates are not in the valid range!")

    # Convert coordinates into numbers of tiles

    # SRTM Tiles with size of 5°
    d_lon = 5
    d_lat = 5

    lon_max = 181
    lat_max = 61

    #  dx = lon + lon_max
    #  strm_dx = d_lon

    lon_srtm = math.ceil((lon + lon_max) / d_lon)
    if lon_srtm == 73:
        lon_srtm = 72

    lat_srtm = math.ceil(abs((lat - lat_max) / d_lat))
    if lat_srtm == 25:
        lat_srtm = 24

    # Right file name for the tile
    global tile_name
    tile_name = f"srtm_{lon_srtm:02d}_{lat_srtm:02d}"
    url = "http://srtm.csi.cgiar.org/wp-content/uploads/files/srtm_5x5/TIFF/"
    global url_tile
    url_tile = url + tile_name + ".zip"

    # Download Tile
    global newfilename
    newfilename = "DEM_" + tile_name + ".zip"

    # return tile


def more_tiles(lon1, lon2, lat1, lat2):

    if lon2 < lon1 or lat2 < lat1:
        raise NameError("The range of coordinates is not valid.")

    tiles = []

    for lon in range(lon1, lon2 + 5, 5):
        for lat in range(lat1, lat2 + 5, 5):
            coordinates2tilepath(lon, lat)
            tiles.append(newfilename)

    n_tiles = len(tiles)

    y_n = input(
        "There are "
        + str(n_tiles)
        + " tiles to download. Are you sure, you want to download them? y/n"
    )

    if y_n == "n":
        print("You stopped downloading.")

    if y_n == "y":
        for lon in range(lon1, lon2 + 5, 5):
            for lat in range(lat1, lat2 + 5, 5):
                coordinates2tilepath(lon, lat)
                download_tile()


def download_tile():
    # list all folders of current working directory
    folders = os.listdir(path)

    if newfilename in folders:
        print("The tile " + newfilename + " is in your directory yet.")
    else:
        urllib.request.urlretrieve(url_tile, (path + "/" + newfilename))
        tile_size = os.path.getsize(path + "/" + newfilename)
        print(
            "The file "
            + newfilename
            + " is downloaded, it has a size of "
            + str(tile_size / 1024 / 1000)
            + " MB."
        )


if __name__ == "__main__":
    # ask for number of arguments

    arg = list(sys.argv)

    if "--output-dir" in arg:
        path = sys.argv[-1]
        arg = arg[0:-2]
    else:
        path = os.getcwd()

    n_arg = len(arg)

    if n_arg == 3:
        lon = int(sys.argv[1])
        lat = int(sys.argv[2])

        # tile = coordinates2tilepath(lon, lat)
        # download_tile(tile)
        coordinates2tilepath(lon, lat)
        download_tile()
    elif n_arg == 5:
        lon1 = int(sys.argv[1])
        lat1 = int(sys.argv[2])
        lon2 = int(sys.argv[3])
        lat2 = int(sys.argv[4])
        more_tiles(lon1, lon2, lat1, lat2)
