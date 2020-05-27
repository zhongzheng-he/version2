# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 10:11:23 2017

@author: broche
"""

from PyMca5.PyMca import PyMcaQt as qt


class DicomReaderGUI(qt.QWidget):

    def __init__(self, scan_list, parent=None,):
        qt.QWidget.__init__(self, parent)

        self.mainLayout = qt.QGridLayout()
        self.scan_list = scan_list
        self.widgetList = []

        for scan in self.scan_list:
            w = qt.QCheckBox(scan)
            self.widgetList.append(w)

        self.startImporting = qt.QPushButton("OK")

        index = 0
        for w in self.widgetList:
            w.setChecked(True)
            self.mainLayout.addWidget(w,index%15,int(index/15))
            index += 1

        self.mainLayout.addWidget(self.startImporting )
        self.setLayout(self.mainLayout)

class MatReaderGUI(qt.QWidget):

    def __init__(self, scan_list, parent=None,):
        qt.QWidget.__init__(self, parent)

        self.mainLayout = qt.QGridLayout()
        self.scan_list = scan_list
        self.widgetList = []

        for scan in self.scan_list:
            w = qt.QCheckBox(scan)
            self.widgetList.append(w)

        self.startImporting = qt.QPushButton("OK")

        for w in self.widgetList:
            self.mainLayout.addWidget(w)

        self.mainLayout.addWidget(self.startImporting )
        self.setLayout(self.mainLayout)