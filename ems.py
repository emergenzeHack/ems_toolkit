import os
import get_ems_zips
import merge_ems_zips

###############################################################################
# CONFIGURATION
# configure the EMS tags that you want as ZIP vector data
# example -> emergency_tags=["EMSR238", "EMSR239", "EMSR240"]
# example -> elements = ['area_of_interest', 'crisis_information_poly', 'hydrography_line', 'hydrography_poly']
emergency_tags=["EMSR238"]
elements = ['area_of_interest', 'crisis_information_poly', 'hydrography_line', 'hydrography_poly']
###############################################################################

#set current path
#os.chdir(os.getcwd())
#download data
get_ems_zips.get_ems_zips(emergency_tags)
#merging shapefiles
merge_ems_zips.merge_ems_zips(emergency_tags,elements)


