#this script donwload ZIP files of EMS setting a list of EMS tags in the emergency_tags (see example)
#!/usr/bin/env python

import requests
#import requests.cookies
#import urllib2
#import urllib
#from cookielib import CookieJar
import html5lib
import os
import subprocess
#import shlex
from bs4 import BeautifulSoup



###############################################################################
# CONFIGURATION
# configure the EMS tags that you want as ZIP vector data
emergency_tags=["EMSR238"]
###############################################################################

def get_zip_links(archive_url):

    # create response object
    r = requests.get(archive_url)

    # create beautiful-soup object
    soup = BeautifulSoup(r.content,'html5lib')

    # find all links on web-page
    links = soup.findAll('a')

    # filter the link sending with .zip
    zip_links = [archive_url + link['href'] for link in links if link['href'].endswith('zip')]

    return zip_links

def download_zip_series(zip_links):

    #iterate through all links in zip_links and download them one by one
    for link in zip_links:

        #obtain filename
        file_name = link.split('/')[-1]

        command="curl -s -c cookie "+'"'+link+'"'
        os.system(command)

        command1="curl -b cookie -s "+'"'+link+'" -H "Origin: http://emergency.copernicus.eu" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36" -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Cache-Control: max-age=0" -H "Referer: '+link+'" -H "Connection: keep-alive" --data "confirmation=1^&op=+Download+file+^&form_build_id=form-wfWtSFuhPbanIpxEiVM8LPHnvLF5LEOuakUYLcXkCeI^&form_id=emsmapping_disclaimer_download_form" --compressed > '+ file_name
        print command1

        os.system(command1)

        #subprocess.call(["./download.sh", link, file_name])
        #session = requests.Session()
        #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
        #response = session.get("http://emergency.copernicus.eu/")

        #set up the Session object, so as to preserve the cookies between requests.
        #now begin download
        #response1 = session.get(link, cookies = response.cookies)
        #zipcontent = response1.content

        #write file
        #file_ = open(file_name, 'w')
        #file_.write(zipcontent)
        #file_.close()

        print "%s downloaded!\n"%file_name

    return

if __name__ == "__main__":

    for ems in emergency_tags:        # main

        archive_url = "http://emergency.copernicus.eu/mapping/list-of-components/" + ems

        # getting all zip links
        zip_links = get_zip_links(archive_url)

        # download all zip files
        download_zip_series(zip_links)

    print "Done. All zip files are downloaded!"

