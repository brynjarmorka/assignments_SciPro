"""
notes and smaller tests from info from week 3

"""

#%% 01 modules,import mechanism, namespace(s), scopes

print(f"info on dir:\n")
help(dir())

#
import sys

sys.path
#
# sys.path.append(
#     "C:\\Users\\Brynjar\\Desktop\\SciProg\\assignments_SciPro\\week03\\matplotlib.py"
# ) # was changed to fake_matplotlib.py after the test
#
# sys.path
#
# import matplotlib
#
# print(matplotlib.check_string)
# # AttributeError: module 'matplotlib' has no attribute 'check_string'
# # Because python imports the right matpotlib first


#%%

# from pathlib import Path
#
# data_folder = Path("source_data/text_files/")
#
# file_to_open = data_folder / "raw_data.txt"
#
# print(file_to_open.read_text())
