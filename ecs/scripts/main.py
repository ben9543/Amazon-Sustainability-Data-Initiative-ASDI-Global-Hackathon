import netcdf4_to_json
import s3_dataset


# Variables example
REGION = "eu-central-1"
BUCKET_NAME = "meeo-s5p"
PREFIX="NRTI/L2__CO____/2022/08/10/"
FILE_DESTINATION = "ncfiles/"
CSV_RESULT_DESTINATION = "csv/"
JSON_RESULT_DESTINATION = "json/"


# Connect to the data set & Downloading files
dataset_client= s3_dataset.S3DataSetClient(REGION, BUCKET_NAME, PREFIX)
# dataset_client.downloadFiles(FILE_DESTINATION)

# Create CSV files
# netcdf4_to_csv.writeFiles(folder_path=FILE_DESTINATION, result_path = CSV_RESULT_DESTINATION)

# Create JSON files
netcdf4_to_json.writeFiles(folder_path=FILE_DESTINATION, result_path = JSON_RESULT_DESTINATION)