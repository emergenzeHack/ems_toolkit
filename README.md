# Copernicus EMS ToolKIT
A set of scripts and opensource tools to work with open data produced by the Copernicus Emergency Management Service.

Usage: Configure the app in ems.py as described:
- Configure in the script TAG of emergencies ex: emergency_tags=["EMSRXXX","EMSRYYY"].
- Configure in elements array the data of interest.
- Configure in pics_conf array the type of images (jpg, tif, pdf) and the resolution (100,200,300)
- Run "python ems.py" to download data and merge shapefiles

# get_ems_zips.py

Script for mass-downloading of vector package ZIP files of EMS. The script use CURL.
The vector packages typically contain shapefiles and KMZs with individual layers, incl. 'crisis_information_poly'.

# get_ems_pics.py

Script for mass-downloading of rasterized map sheets of EMS. The script use CURL.
The map sheets are available in GeoTIFF, JPEG or PDF formats in 100 DPI, 200 DPI and 300 DPI resulutions. PDF format is layered, i.e. suitable for "flickering".

# merge_ems_zips.py

The script merges all shape files in ZIP files of multiple emergencies in a folder. Stores all ZIP files of one or more emergencies.
Script realized starting from [this script](https://github.com/emergenzeHack/terremotocentro_geodata/blob/gh-pages/CopernicusEMS/scripts/copernicus_EMSR.py), thanks to [geofrizz](https://github.com/geofrizz).
