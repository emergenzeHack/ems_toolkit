#!/usr/bin/python
# -*- coding: utf-8 -*-
#script to be executed in folder where EMS ZIP files are stored
#created starting from https://github.com/emergenzeHack/terremotocentro_geodata/blob/gh-pages/CopernicusEMS/scripts/copernicus_EMSR.py

import os
import zipfile
import shutil
import glob
import shapefile


###############################################################################
#input ZIP files (default current path)
folder_input_zip = os.path.dirname(os.path.abspath(__file__)) + "/"
#temporary ZIP files
folder_output_zip = os.path.dirname(os.path.abspath(__file__)) + "/temp/"

#shape are in the temp folder
folder_input_shp = folder_output_zip
#shapefiles output default are current path
folder_output_shp = os.path.dirname(os.path.abspath(__file__)) + "/"

#path for merging
folder_input_merge = os.path.dirname(os.path.abspath(__file__)) + "/"
folder_output_merge = os.path.dirname(os.path.abspath(__file__)) + "/"
###############################################################################

def create_path(dirname):
    try:
        os.makedirs(dirname)
    except OSError:
        if os.path.exists(dirname):
            # We are nearly safe
            pass
        else:
            # There was an error on creation, so make sure we know about it
            raise

def extract_zipped_files (file_name):
    #pass
    print file_name
    file_name_in=folder_input_zip+file_name
    with zipfile.ZipFile(file_name_in, "r") as z:
        z.extractall(folder_output_zip)

def clean_folder (emergency_tags):
    #pass
    folder_del = folder_output_zip + "*.*"
    files = sorted(glob.glob(folder_del))
    for f in files:
        os.remove(f)
    for element in emergency_tags:
        folder_del = folder_output_shp + element + "/*.*"
        files = sorted(glob.glob(folder_del))
        for f in files:
            os.remove(f)
    for element in emergency_tags:
        folder_del = folder_output_merge + element + "_merged.*"
        files = sorted(glob.glob(folder_del))
        for f in files:
            os.remove(f)

def merge_ems_zips (emergency_tags,elements):
    clean_folder(emergency_tags)
    #exit()

    for tags in emergency_tags:
        create_path(folder_input_zip+tags+"_merged")
        for category in elements:
            create_path(folder_input_zip+tags+ "_" + category)

    for file in sorted(os.listdir(folder_input_zip)):
        for tags in emergency_tags:
            if tags in file:
                if file.endswith(".zip"):
                    extract_zipped_files(file)

    # move files
    for file in sorted(os.listdir(folder_input_shp)):
        for ems in emergency_tags:
            if ems in file:
                for category in elements:
                    if category in file:
                        file_move_name_in = folder_input_shp + file
                        file_move_name_out = folder_output_shp + ems + "_" + category + "/" + file
                        shutil.move(file_move_name_in,file_move_name_out)

    # merge files
    for ems in emergency_tags:
        for category in elements:
            folder_input_in = folder_input_merge + ems + "_" + category + '/*.shp'
            folder_input_out = folder_output_merge + ems + "_" + category + '_merged.shp'
            files = sorted(glob.glob(folder_input_in))
            w = shapefile.Writer()
            for f in files:
                r = shapefile.Reader(f)
                w._shapes.extend(r.shapes())
                w.records.extend(r.records())
                w.fields = list(r.fields)
            w.save(folder_input_out)

            folder_input_in = folder_input_merge + ems + "_" + category + '/*.prj'
            folder_input_out = folder_output_merge + ems + "_" + category + '_merged.prj'
            files = sorted(glob.glob(folder_input_in))
            for f in files:
                shutil.copy(f,folder_input_out)
                break
        #move files
        sh = sorted(glob.glob(folder_input_merge+"/*.shp"))
        for file in sh:
            shutil.move(file, folder_output_merge + ems + "_merged")
        sh = sorted(glob.glob(folder_input_merge+"/*.dbf"))
        for file in sh:
            shutil.move(file, folder_output_merge + ems + "_merged")
        sh = sorted(glob.glob(folder_input_merge+"/*.shx"))
        for file in sh:
            shutil.move(file, folder_output_merge + ems + "_merged")
        sh = sorted(glob.glob(folder_input_merge+"/*.prj"))
        for file in sh:
            shutil.move(file, folder_output_merge + ems + "_merged")

    print "Merged all"
