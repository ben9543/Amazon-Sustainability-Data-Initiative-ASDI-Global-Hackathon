import json
import os
import glob
from netCDF4 import Dataset

# files => list of strings(filepaths)
DEFAULT_PATH = "json/"

def deleteFiles(folder_path):
    pass

def writeFiles(folder_path, result_path = DEFAULT_PATH):
    """
    folder_path:
    result_path:
    """

    files = glob.glob(folder_path+"*.nc")

    if not os.path.exists(result_path):
        os.mkdir(result_path)
    
    for k, file_path in enumerate(files):

        # Extract data
        r = extractFile(file_path)
   
        # Save as JSON file
        with open(f"{result_path}/{k}.json", 'w') as f:
            json.dump({"data": r}, f)
        
        print("Saved " + f"{k}.json")

def extractFile(file_path):

    result = []

    rootgrp = Dataset(file_path, "r", format="NETCDF4")
    rtgp = rootgrp["PRODUCT"]

    latitude = rtgp.variables['latitude'][:][0]
    longitude = rtgp.variables['longitude'][:][0]
    scanline = rtgp.variables['scanline'][:]
    ground_pixel = rtgp.variables['ground_pixel'][:]
    
    # Appending to list
    for s in range(len(scanline)):
        for g in range(len(ground_pixel)):
            lat = latitude[s][g]
            lon = longitude[s][g]
            res = rtgp.variables['carbonmonoxide_total_column'][0, s, g]

            # Converting Numpy Float to Python Float for JSON serializing
            result.append({'lat':float(lat), 'lon':float(lon), 'carb_total': float(res.data.item())})

    # Close the root group
    rootgrp.close()
    
    return result