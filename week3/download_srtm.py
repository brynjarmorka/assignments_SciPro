"""

File for dowloading SRTM files.
Files found at srtm.csi.cgiar.org/wp-content/uploads/files/srtm_5x5/TIFF/srtm_{LO}_{LA}.zip
longitudes (starting at 180° West)
latitudes (starting at 60° North and going southwards)
# North is positive
# East is positive
# West is negative
# South is negative

"""

#%% imports
import os.path
import sys
import math
import urllib.request
from os import listdir
from os.path import isfile, join
from pathlib import Path

#%%
def validate_two_coordinates(lng, lat):
    """
    Task A. Checks if the coordinate range is [-180,180] and {-60,60]
    :return: bool
    """
    min_lo, max_lo, min_la, max_la = -180, 180, -60, 60
    return min_lo <= lng <= max_la and min_la <= lat <= max_la


def coord_to_file_nr(coord):
    """
    Translates coordinates to STRM file number
    :param coord: list [lon, lat], type str
    :return: list [lng_tile_nr, lat_tile_nr], type int. OR empty string
    """
    try:
        lng = round(float(coord[0]))
        lat = round(float(coord[1]))
    except TypeError:
        print("Your input coordinates are not valid")
        return "", ""
    if validate_two_coordinates(lng, lat):  # if the values at within the valid range
        lng_tile_nr = math.ceil((lng + 181) / 5)  # lng is 1-indexed
        if lng_tile_nr == 73:
            lng_tile_nr = 72  # if input is 180+180 = 360
        lat_tile_nr = math.ceil((abs(lat - 61)) / 5)  # lat is shifted 60deg north
        return lng_tile_nr, lat_tile_nr
    else:
        print("Not valid coordinates")
        return "", ""


def download_file(url, filename, selected_path=Path(".")):
    """
    downloading the file, if the file is not in the current wd
    :param url: str
    :param filename: str
    :param selected_path: path for download, standard is wd
    :return: None
    """
    if filename:  # checks if the filename is empty
        only_files = [
            f for f in listdir(selected_path) if isfile(join(selected_path, f))
        ]
        if filename in only_files:
            print("You already have this file.")
        else:
            urllib.request.urlretrieve(url, selected_path / filename)
    else:
        print("Some coordinates were not valid")


def single_file_download(lng_nr, lat_nr, selected_path):
    """
    Task A and B together, for running single files
    :return:
    """
    filename = f"srtm_{lng_nr:02d}_{lat_nr:02d}.zip"
    url = "http://srtm.csi.cgiar.org/wp-content/uploads/files/srtm_5x5/TIFF/" + filename
    try:
        download_file(url, filename, selected_path)
        print(
            f"Successful download of '{filename}'! Filesize: {round(os.path.getsize(selected_path / filename)/1024**2, 2)} MB"
        )
    except urllib.error.HTTPError as exception:
        print(f"Coordinates not avaliable, probably in the ocean. ({exception})")


def run_this_script():
    print(sys.argv)
    coordinates = sys.argv[1:]
    selected_path = Path(".")
    if "--output-dir" in coordinates:
        selected_path = Path(coordinates[-1])  # last user input element
        if selected_path.exists():
            coordinates = coordinates[:-2]
        else:
            sys.exit("Selected path does not exist.\n")
    print(coordinates)
    if len(coordinates) == 2:
        lng_nr, lat_nr = coord_to_file_nr(coordinates)
        if lng_nr:  # lng_nr is empty if the input was invalid
            single_file_download(lng_nr, lat_nr, selected_path)
    elif len(coordinates) == 4:
        lng_start, lat_start = coord_to_file_nr(coordinates[:2])
        lng_end, lat_end = coord_to_file_nr(coordinates[2:])
        # handling if the range is negative direction
        lng = [lng_start, lng_end]
        lat = [lat_start, lat_end]
        lng.sort()
        lat.sort()
        tiles_list = []
        for lng_tile in range(lng[0], lng[1]):
            for lat_tile in range(lat[0], lat[1]):
                tiles_list.append([lng_tile, lat_tile])
        print(tiles_list)
        file_amount = len(tiles_list)
        download_all = input(f"Do you want to download {file_amount} files?(y/n) ")
        if download_all.lower() == "y":
            for tile in tiles_list:
                single_file_download(tile[0], tile[1], selected_path)


run_this_script()
