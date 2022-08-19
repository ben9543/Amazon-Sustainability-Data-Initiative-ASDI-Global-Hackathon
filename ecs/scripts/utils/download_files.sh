#!/bin/bash

year = 2022
month = 8
day = 10
hour = 10
minutes = 10
seconds = 10

mission_id = "S5P"
file_class = "NRTI"
file_type = "L2__CO____"

# <yyyymmddThhmmss>_<YYYYMMDDTHHMMSS>_<ooooo>_<cc>_<pppppp>_< YYYYMMDDTHHMMSS >
# instance_id = "$yyyymmddThhmmss_$YYYYMMDDTHHMMSS_$ooooo_$cc_$pppppp_$last"

filename = "$mission_id"
aws s3 cp "s3://meeo-s5p/NRTI/L2__CO____/2022/08/10/$filename --no-sign-request"