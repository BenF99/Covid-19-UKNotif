#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Ben F
# Created Date: Mon April 27 15:30:00 GMT 2020
# =============================================================================
# =============================================================================
# Imports

import urllib.request, json
import time

from win10toast import ToastNotifier

# =============================================================================


class coronaVirusGB:

    url = "https://api.thevirustracker.com/free-api?countryTotal=GB"

    def __init__(self):
        self.total_cases = None
        self.total_deaths = None
        self.total_new_cases_today = None
        self.total_new_deaths_today = None

    def readJson(self):
        with urllib.request.urlopen(coronaVirusGB.url) as url:
            data = json.loads(url.read().decode())
            return data

    def updateData(self):
        data = self.readJson()
        self.total_cases = data['countrydata'][0]['total_cases']
        self.total_deaths = data['countrydata'][0]['total_deaths']
        self.total_new_cases_today = data['countrydata'][0]['total_new_cases_today']
        self.total_new_deaths_today = data['countrydata'][0]['total_new_deaths_today']
        

cv = coronaVirusGB()

while (cv.total_new_cases_today or cv.total_new_deaths_today) == 0 or (cv.total_new_cases_today or cv.total_new_deaths_today) == None:
    cv.updateData()
    print ("Updated...")
    time.sleep(1800)

toaster = ToastNotifier()
toaster.show_toast("COVID-19 Update!", str(cv.total_new_cases_today) + " New Cases | " + str(cv.total_new_deaths_today) + " New Deaths | " + str(cv.total_deaths) + " Total Deaths", threaded = True,
                   icon_path=None, duration=15)





    

    
