#example from aborruso
#curl -s -c cookie  "http://emergency.copernicus.eu/mapping/download/137779/EMSR190_32ACQUASANTATERME_GRADING_OVERVIEW_v1_vector.zip"
#curl -b cookie -s "http://emergency.copernicus.eu/mapping/download/137779/EMSR190_32ACQUASANTATERME_GRADING_OVERVIEW_v1_vector.zip" -H "Origin: http://emergency.copernicus.eu" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36" -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Cache-Control: max-age=0" -H "Referer: http://emergency.copernicus.eu/mapping/download/137779/EMSR190_32ACQUASANTATERME_GRADING_OVERVIEW_v1_vector.zip" -H "Connection: keep-alive" --data "confirmation=1^&op=+Download+file+^&form_build_id=form-wfWtSFuhPbanIpxEiVM8LPHnvLF5LEOuakUYLcXkCeI^&form_id=emsmapping_disclaimer_download_form" --compressed > EMSR190_32ACQUASANTATERME_GRADING_OVERVIEW_v1_vector.zip

#!/bin/bash

LINK=$1
FILE_NAME=$2

curl -s -c cookie $LINK

curl -b cookie -s $LINK -H "Origin: http://emergency.copernicus.eu" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36" -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Cache-Control: max-age=0" -H "Referer: $LINK" -H "Connection: keep-alive" --data "confirmation=1^&op=+Download+file+^&form_build_id=form-wfWtSFuhPbanIpxEiVM8LPHnvLF5LEOuakUYLcXkCeI^&form_id=emsmapping_disclaimer_download_form" --compressed > $FILE_NAME