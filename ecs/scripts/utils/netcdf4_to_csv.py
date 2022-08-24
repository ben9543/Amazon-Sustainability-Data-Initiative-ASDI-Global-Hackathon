from netCDF4 import Dataset
import csv
import glob

# files => list of strings(filepaths)
DEFAULT_PATH = "csv/result.csv"

def deleteFiles(folder_path):
    pass

def writeFiles(folder_path, result_path):
    """
    
    """
    files = glob.glob(folder_path+"*.nc")
    for file_path in files:
        writeFile(file_path, result_path)

def writeFile(file_path, saveTo = DEFAULT_PATH):
    
    ''' dimensions
    {
        'scanline': <class 'netCDF4._netCDF4.Dimension'>: name = 'scanline', size = 331, 
        'ground_pixel': <class 'netCDF4._netCDF4.Dimension'>: name = 'ground_pixel', size = 215, 
        'corner': <class 'netCDF4._netCDF4.Dimension'>: name = 'corner', size = 4, 
        'time': <class 'netCDF4._netCDF4.Dimension'>: name = 'time', size = 1, 
        'layer': <class 'netCDF4._netCDF4.Dimension'>: name = 'layer', size = 50
    }

    variables
    scanline
    ground_pixel
    time
    corner
    layer
    delta_time
    time_utc
    qa_value
    latitude
    longitude
    carbonmonoxide_total_column
    carbonmonoxide_total_column_precision
    carbonmonoxide_total_column_corrected
    '''

    rootgrp = Dataset(file_path, "r", format="NETCDF4")
    rtgp = rootgrp["PRODUCT"]

    latitude = rtgp.variables['latitude'][:][0]
    longitude = rtgp.variables['longitude'][:][0]
    scanline = rtgp.variables['scanline'][:]
    ground_pixel = rtgp.variables['ground_pixel'][:]
    
    # Writing into CSV format
    with open(saveTo, 'a', newline='') as csvfile:
        fieldnames = ['lat', 'lon', 'carb_total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for s in range(len(scanline)):
            for g in range(len(ground_pixel)):
                lat = latitude[s][g]
                lon = longitude[s][g]
                res = rtgp.variables['carbonmonoxide_total_column'][0, s, g]
                writer.writerow({'lat':lat, 'lon':lon, 'carb_total':res})
    rootgrp.close()

    #df = pd.DataFrame(0, columns=['Emission', ])