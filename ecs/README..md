# ECS

## Roles

#### ECS Task Role

- `ECSTaskRoleS3Upload`: Allow ECS to upload a csv file to a specifed bucket.


## Sentinel 5P

#### Filename Convention

- [Link](https://sentinels.copernicus.eu/documents/247904/2506504/FFS-Tailoring-Sentinel-5P.pdf/fa96b324-4f9b-47b3-b57a-921a7c47f374?t=1528905632000)


`<MMM>_<CCCC>_<TTTTTTTTTT>_<instance ID>`

```
<MMM> = Mission ID (3 characters)
<CCCC> = File Class (4 characters)
<TTTTTTTTT> = File Type (10 characters)
<instance ID> = File Instance ID (63 or 47 characters)
```

- File Instance ID

For S5P, two shapes are assumed for the File Instance ID. The first one is used for
L0/L1B/L2 science data products, including so called L1B calibration and engineering
products, which are produced internally by the PDGS. The second one is used for the
auxiliary data products that are produced outside of the PDGS, either statically or
dynamically.

For science data products **(with the File Type set “L0__”/“L1B_”/“L2__”)**, the File
Instance ID consists of 63 characters

`<yyyymmddThhmmss>_<YYYYMMDDTHHMMSS>_<ooooo>_<cc>_<pppppp>_< YYYYMMDDTHHMMSS >`

```
<yyyymmddThhmmss>: product start sensing time, consisting of 15 characters,
either uppercase letters or digits:
• 8 digits for the date: “yyyymmdd”, year, month, day
• 1 uppercase T: “T”
• 6 digits for the time: “hhmmss”, hour, minutes, seconds
<YYYYMMDDTHHMMSS>: product stop sensing time, consisting of 15 characters,
either uppercase letters or digits:
• 8 digits for the date: “YYYYMMDD”, year, month, day
• 1 uppercase T: “T”
• 6 digits for the time: “HHMMSS”, hour, minutes, seconds
<ooooo>: absolute orbit number, consisting of 5 digits, starting at 00001 (qfirst
ascending node crossing after spacecraft separation),
<cc>: collection number, consisting of 2 digits, starting at 01,
<pppppp>: processor version number, consisting of 6 digits, with the first 2 digits
for major updates, the next 2 digits for minor updates and the last 2 digits for new
releases, i.e. 010203 for processor version 1.2.3,

YYYYMMDDTHHMMSS >: production (start) time, consisting of 15 characters,
either uppercase letters or digits:
• 8 digits for the date: “YYYYMMDD”, year, month, day
• 1 uppercase T: “T”
• 6 digits for the time: “HHMMSS”, hour, minutes, seconds
```


- Fixed values: 
  - Mission ID: `S5P`
  - File Class: `NRTI`
  - File Type:
    - `L2__CO____`: Carbon Monoxide (CO) total column
    - `L2__CH4___`: Methane (CH4) total column
  - Instance ID
    - 