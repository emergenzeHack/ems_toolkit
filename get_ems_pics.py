#this script donwload PICS files of EMS
#!/usr/bin/env python

import requests
import html5lib
import os
import subprocess
from bs4 import BeautifulSoup


def get_pics_links(archive_url, pics_conf):

    # create response object
    r = requests.get(archive_url)

    # create beautiful-soup object
    soup = BeautifulSoup(r.content,'html5lib')
    # find all links on web-page
    links = soup.findAll('a')
    # filter the links ending with .pics
    pics_links = [link['href'] for link in links if link['href'].endswith(pics_conf[1]+'dpi'+'.'+pics_conf[0])]

    return pics_links

def download_pics_series(pics_links):
    print pics_links
    #iterate through all links in zip_links and download them one by one
    for link in pics_links:

        #obtain filename
        file_name = link.split('/')[-1]

        command="curl -# -O "+'"'+link+'" -H "User-Agent: EMS Toolkit (dfe3b314c95db26fafbc758c17db76ec)" -H "Connection: keep-alive" '
        os.system(command)

        print "%s downloaded!\n"%file_name
    return

def get_ems_pics (emergency_tags, pics_conf):

    for ems in emergency_tags:        # main

        archive_url = "http://emergency.copernicus.eu/mapping/list-of-components/" + ems

        # getting all zip links
        pics_links = get_pics_links(archive_url, pics_conf)
        # download all zip files
        download_pics_series(pics_links)

    print "Done. All pics files are downloaded!"

