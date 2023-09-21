# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 11:09:26 2022

@author: obandohe
"""

import numpy as np

class readlas3:
    'Read LAS version 3 files.'
    def __init__(self, filename, version = '3.0', wrap = 'False',
                 delim = ' '):
        self.filename = filename
        f = open(self.filename,'r')
        read = True
        while read:
            self.line = f.readline()
            if self.line[:2] == '~V':
                self.version = f.readline().split()[1]
                self.wrap = f.readline().split()[1]
                self.delim = f.readline().split()[1]
                # ! insert other delimiters
                if self.delim == 'SPACE':
                    self.delim = ' '
                # other info is skipped for now
                read = False
                f.close()

    def lasheader(self):
        'read las3 header'
        f = open(self.filename,'r')
        read = True
        self.header = {}
        while read:
            self.line = f.readline()
            if self.line[:2] == '~W':
                readitems = True
                print('yes')
                while readitems:                    
                    self.line = f.readline()
                    if self.line[0] == '#' or self.line[0] == ' ':
                        readitems = False
                        read = False
                        f.close()   
                    else:
                        self.key = self.line.split('.')[0]
                        #self.unit = self.line.split('.')[1] # improve
                        try:
                            self.val = float(self.line.split()[1])
                        except ValueError:
                            self.val = ' '
                        self.desc = self.line.split(':')[-1][:-1]
                        self.header[self.key] = [self.val,self.desc]
                        
        return self.header

    def readdata(self):
        self.data = {}
        f = open(self.filename,'r')
        read = True
        count = 1
        self.eof = 0
        while read:
            # first read log definition
            self.line = f.readline()

            if self.line[:15] == '~LOG_DEFINITION':
                print('yes')
                self.data['LOG_DEFINITION['+str(count)+']'] = {}
                readitems = True
                self.item = []
                self.dim = []
                while readitems:
                    self.readitemline = f.readline()
                    try:
                        if self.readitemline[0] == '#' or \
                           self.readitemline[0] == ' ' or self.readitemline[0] == '~':
                            readitems = False
                        else:
                            self.item.append(self.readitemline.split('.')[0])
                            self.dim.append(self.readitemline.split()[-1])
                    except IndexError:
                        readitems = False
                        pass
                for i in range(len(self.item)):
                    self.data['LOG_DEFINITION['+str(count)+']'][self.item[i]] = [self.dim[i]]
                    # first fill with units
            elif self.line[:9] == '~LOG_DATA':
                readdata = True
                self.datalines = [[] for i in range(len(self.item))] 
                while readdata:
                    self.readdataline = f.readline().split()# change later; delim
                    if len(self.readdataline) > 1:
                        for i in range(len(self.readdataline)):
                            self.datalines[i].append(float(self.readdataline[i]))
                    else:
                        readdata = False
                for i in range(len(self.item)):
                    self.data['LOG_DEFINITION['+str(count)+']'][self.item[i]].append(np.array(self.datalines[i]))
                count = count + 1
                self.eof = 0
                    
            if len(self.line) < 2:
                self.eof = self.eof + 1
            if self.eof > 5:
                read = False

        return self.data
                    
