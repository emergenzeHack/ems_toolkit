# EMS ToolKIT
A set of script and tools opensource to manage EMS Copernicus Service
(idea by [iltempe](https://github.com/iltempe))

Usage: Configure the app in ems.py as described. Run "python ems.py" to download data and merge shapefiles


# merge_ems_zips.py

Script realized starting from [this script](https://github.com/emergenzeHack/terremotocentro_geodata/blob/gh-pages/CopernicusEMS/scripts/copernicus_EMSR.py), thanks to [geofrizz](https://github.com/geofrizz).

The script merge all shape files in zips file of multiple emergencies in a folder. Store all zip files of one or more emergencies. Configure in the script TAG of emergencies ex: emergency_tags=["EMSRXXX","EMSRYYY"]. Configure in elements array the data of interest. Run python script.

# get_ems_zips.py

Script realized for mass download of ZIPs package vector files of EMS. Configure in the script TAG of emergencies ex: emergency_tags=["EMSRXXX","EMSRYYY"]. Run the script. The script use CURL (see as example download.sh bash thanks to [aborruso](https://github.com/aborruso) for the curl operations and cookie management)
