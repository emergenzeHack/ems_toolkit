# EMS ToolKIT
A set of scripts and opensource tools to work with open data produced by the Copernicus Emergency Management Service(designed by [iltempe](https://github.com/iltempe))

Usage: Configure the app in ems.py as described. Configure in the script TAG of emergencies ex: emergency_tags=["EMSRXXX","EMSRYYY"]. Configure in elements array the data of interest. Run "python ems.py" to download data and merge shapefiles


# get_ems_zips.py

Script realized for mass download of ZIPs package vector files of EMS. The script use CURL (thanks to [aborruso](https://github.com/aborruso) for the curl operations for cookie management)

# merge_ems_zips.py

The script merge all shape files in zips file of multiple emergencies in a folder. Store all zip files of one or more emergencies.

Script realized starting from [this script](https://github.com/emergenzeHack/terremotocentro_geodata/blob/gh-pages/CopernicusEMS/scripts/copernicus_EMSR.py), thanks to [geofrizz](https://github.com/geofrizz).

