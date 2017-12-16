import os
import get_ems_zips
import merge_ems_zips
import get_ems_pics
import csv

###############################################################################
# CONFIGURATION
# configure the EMS tags that you want as ZIP vector data in first row of conf.csv
# example configure EMSR238 -> emergency_tags=["EMSR238"]
# configure the EMS tags elements that you want to extract as data in second row of conf.csv
# example configure observed_event_a- > elements = ['observed_event_a']
# configure the EMS pics properties in terms of format and resolution that you want to extract as data in third row of conf.csv
# example configure pdf; 300 -> pics_conf = ['pdf', '300'] where first is image extension (pdf, jpg or tif) and second is the resolution (100, 200 or 300)
###############################################################################
def configure(filename):
    ifile = open(filename, "rU")
    reader = csv.reader(ifile, delimiter=";")
    rownum = 0
    a = []
    for row in reader:
        a.append (row)
        rownum += 1
    ifile.close()
    return a

#configure
conf=configure("conf.csv")
emergency_tags=conf[0]
elements=conf[1]
pics_conf=conf[2]

#download data
get_ems_zips.get_ems_zips(emergency_tags)

#download pics
get_ems_pics.get_ems_pics(emergency_tags, pics_conf)

#merging shapefiles
merge_ems_zips.merge_ems_zips(emergency_tags,elements)




