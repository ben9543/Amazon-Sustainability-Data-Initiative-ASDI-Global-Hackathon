import fsspec
import xarray as xr
from datetime import date

# The oldest time format: "1984-01-31"
def getTimeDecimals(year, month):
    default_year = 1984
    curr_year = date.today().year
    curr_month = date.today().month

    if(year < 0 or month < 0 or month > 13):
        raise IndexError()
    elif(year < default_year):
        raise IndexError()
    elif(year > curr_year ):
        raise IndexError()
    elif(year == curr_year and month > curr_month):
        raise IndexError()

    time = ((year - default_year) * 12) + (month-1)
    return time

def getLatLonDecimals(lat, lon):
    lat_default = -89.5
    lon_default = -179.5

    if(lat < lat_default or lat > lat_default*(-1)):
        raise IndexError("Latitude should be between -89.5 ... 89.5")
    elif(lon < lon_default or lon > lon_default*(-1)):
        raise IndexError("Longitude should be between -179.5 ... 179.5")

    lat = round(lat - lat_default)
    lon = round(lon - lon_default)

    return (lat, lon)

# 'ds' should be XArray.DataSet object
# 'time' should contain a string with a format of: "YYYY-MM-DD"
def getSinglePointData(ds, datavar, year, month, lat, lon):

    # Convert lat & lon to the valid index
    decimal_lat_lon = getLatLonDecimals(lat, lon)
    lat, lon = decimal_lat_lon[0], decimal_lat_lon[1]

    # Get the valid time index
    time = getTimeDecimals(year, month)

    data = ds[datavar][time][lat][lon] # (time: 456, lat: 180, lon: 360)
    return data.values

# Fetching S3
filepath = 'https://power-analysis-ready-datastore.s3.amazonaws.com/power_901_monthly_radiation_utc.zarr/'
filepath_mapped = fsspec.get_mapper(filepath)
ds = xr.open_zarr(store=filepath_mapped, consolidated=True)

# Fixed values
year = 2021
lat = 33.7701
lon = -118.1937
datavar = "ALLSKY_NKT"

# Main loop
for month in range(1, 13):
    res = getSinglePointData(ds=ds, datavar=datavar, year=year, month=month, lat = lat, lon = lon)
    
    print(f"{year}/{month}/31: {res}")
    