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
    print links
    # filter the link sending with .pics
    pics_links = [link['href'] for link in links if link['href'].endswith(pics_conf[1]+'dpi'+'.'+pics_conf[0])]
    return pics_links

def download_pics_series(pics_links):
    print pics_links
    #iterate through all links in zip_links and download them one by one
    for link in pics_links:

        #obtain filename
        file_name = link.split('/')[-1]

        command="curl -O "+'"'+link+'"'
        os.system(command)

        #command1="curl -b cookie -s "+'"'+link+'" -H "Origin: http://emergency.copernicus.eu" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36" -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Cache-Control: max-age=0" -H "Referer: '+link+'" -H "Connection: keep-alive" --data "confirmation=1^&op=+Download+file+^&form_build_id=form-wfWtSFuhPbanIpxEiVM8LPHnvLF5LEOuakUYLcXkCeI^&form_id=emsmapping_disclaimer_download_form" --compressed > '+ file_name
        #os.system(command1)

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

