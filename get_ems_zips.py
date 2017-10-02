#this script donwload ZIP files of EMS setting a list of EMS tags in the emergency_tags (see example)
#!/usr/bin/env python

import requests
import html5lib
import os
import subprocess
from bs4 import BeautifulSoup


def get_zip_links(archive_url):

    # create response object
    r = requests.get(archive_url)

    # create beautiful-soup object
    soup = BeautifulSoup(r.content,'html5lib')

    # find all links on web-page
    links = soup.findAll('a')

    # filter the link sending with .zip
    zip_links = ["http://emergency.copernicus.eu" + link['href'] for link in links if link['href'].endswith('zip')]

    return zip_links

def download_zip_series(zip_links):

    #iterate through all links in zip_links and download them one by one
    for link in zip_links:

        #obtain filename
        file_name = link.split('/')[-1]

        command="curl -# "+'"'+link+'" -H "User-Agent: EMS Toolkit (dfe3b314c95db26fafbc758c17db76ec)" -H "Referer: '+link+'" -H "Connection: keep-alive" > '+ file_name
        os.system(command)

        print "%s downloaded!\n"%file_name
    return

def get_ems_zips (emergency_tags):

    for ems in emergency_tags:        # main

        archive_url = "http://emergency.copernicus.eu/mapping/list-of-components/" + ems

        # getting all zip links
        zip_links = get_zip_links(archive_url)
        print zip_links
        # download all zip files
        download_zip_series(zip_links)

    print "Done. All zip files are downloaded!"

