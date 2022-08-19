import netcdf4_to_csv
import s3_dataset

REGION = "eu-central-1"
BUCKET_NAME = "meeo-s5p"
PREFIX="NRTI/L2__CO____/2022/08/10/"
FILE_DESTINATION = "ncfiles/"
RESULT_DESTINATION = "csv/result.csv"

"""
test_files = [
    "samples/S5P_NRTI_L2__CO_____20220810T003218_20220810T003718_24993_03_020400_20220810T013048.nc",
    "samples/S5P_NRTI_L2__CO_____20220810T055718_20220810T060218_24996_03_020400_20220810T064236.nc",
    #"samples/S5P_NRTI_L2__CO_____20220810T231218_20220810T231718_25006_03_020400_20220810T234906.nc",
    #"samples/S5P_NRTI_L2__CO_____20220810T231718_20220810T232218_25006_03_020400_20220811T011057.nc",
    #"samples/S5P_NRTI_L2__CO_____20220810T232218_20220810T232718_25006_03_020400_20220811T011203.nc"
]
"""

# Connect to the data set & Downloading files
# dataset_client= s3_dataset.S3DataSetClient(REGION, BUCKET_NAME, PREFIX)
# dataset_client.downloadFiles(FILE_DESTINATION)

# Create CSV files
netcdf4_to_csv.writeFiles(folder_path=FILE_DESTINATION, result_path = RESULT_DESTINATION)