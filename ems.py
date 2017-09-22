import os
import get_ems_zips
import merge_ems_zips
import get_ems_pics

###############################################################################
# CONFIGURATION
# configure the EMS tags that you want as ZIP vector data
# example -> emergency_tags=["EMSR238", "EMSR239", "EMSR240"]
emergency_tags=["EMSR238"]
# example -> elements = ['area_of_interest', 'crisis_information_poly', 'hydrography_line', 'hydrography_poly']
elements = ['area_of_interest', 'crisis_information_poly', 'hydrography_line', 'hydrography_poly']
# example -> pics_conf = ['tif', '300'] where first is image extension (pdf, jpg or tif) and second is the resolution (100, 200 or 300)
pics_conf = ['pdf', '300']
###############################################################################

#example of application

#download data
get_ems_zips.get_ems_zips(emergency_tags)

#download pics
get_ems_pics.get_ems_pics(emergency_tags, pics_conf)

#merging shapefiles
merge_ems_zips.merge_ems_zips(emergency_tags,elements)


