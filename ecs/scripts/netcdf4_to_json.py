import json
import os
import glob
import utils.get_dest as get_dest
from netCDF4 import Dataset

# files => list of strings(filepaths)
DEFAULT_PATH = "json/result.json"

def deleteFiles(folder_path):
    pass

def writeFiles(folder_path, result_path = DEFAULT_PATH):
    """
    folder_path:
    result_path:
    """
    result = []
    files = glob.glob(folder_path+"*.nc")
    dest = get_dest.get_dest(result_path)

    if not os.path.exists(dest):
        os.mkdir(dest)
    
    for k, file_path in enumerate(files):
        result.append({f"{k}":extractFile(file_path)})
   
    # Save as JSON file
    with open(result_path, 'a') as f:
        json.dump({"data": result}, f)

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