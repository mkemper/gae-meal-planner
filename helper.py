#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime
import time

class DateHelper(object):

    """ A class to compute and deliver the necessary date and time formats needed by the kemper-meal-planner app """
    
    def __init__(self):
        
        self.day_names = {0:"Montag",1:"Dienstag",2:"Mittwoch",3:"Donnerstag",4:"Freitag",5:"Samstag",6:"Sonntag"}

        self.month_names = {1:"Januar", 2:"Februar", 3:"März", 4:"April", 5:"Mai", 6:"Juni", 7:"Juli", 8:"August", 9:"September", 10:"Oktober", 11:"November", 12:"Dezember"}

        self.actual_day = datetime.date.today()

        self.actual_calendar_week = int(time.strftime("%W",time.struct_time(time.localtime())))

        self.actual_year = int(time.strftime("%Y",time.struct_time(time.localtime())))

    def get_week(self, year, cw):
        first_monday = 4 - datetime.date(year,1,4).weekday()
        monday_of_kw = first_monday + (cw - 1)*7
        list = range(monday_of_kw, monday_of_kw + 7)
        return list

    def get_date(self, year, day_of_year):
        d = datetime.datetime(year,1,1)+datetime.timedelta(day_of_year - 1)
        #date = str(d.year) + "-" + str(d.month) + "-" + str(d.day)
        date = datetime.date(d.year, d.month, d.day)
        return date 
        
    def get_day_name(self, date):
        date = time.strptime(date, "%Y-%m-%d")
        return self.day_names[date[6]]
    
    def get_month_name(self, date):
        date = time.strptime(date, "%Y-%m-%d")
        return self.month_names[date[1]]
    
    def get_year_cw(self, date):
        date = self.gen_date_obj(date)
        year_cw = date.isocalendar()
        #backlink = "/show/"+str(date[0])+"/"+str(date[1])
        return year_cw
    
    def gen_date_obj(self, date):
        date = date.replace('-',' ').split()
        date = datetime.date(int(date[0]),int(date[1]),int(date[2]))
        return date
    
    def get_actual_day(self):
        return actual_day
        
    def get_actual_calendar_week(self):
        return actual_calendar_week
        
    def get_actual_year(self):
        return actual_year

        