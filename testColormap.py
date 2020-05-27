# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 11:11:31 2017

@author: BROCHE
"""
import sys
from PyMca5.PyMca import PyMcaQt as qt

class MyLabel(qt.QWidget):
    
    def __init__(self,text, Rot, fontSize, pos):
        qt.QWidget.__init__(self)
        self.text = text
        self.rot = Rot
        self.ftSize = fontSize 
        self.pos = pos
    
    def paintEvent(self, event):
        painter = qt.QPainter(self)
        painter.setPen(qt.Qt.white)
        if self.rot != 0.0:
            painter.translate(0, 0)
        painter.rotate(self.rot)
        painter.setFont(qt.QFont("times",self.ftSize))
        painter.drawText(self.pos[0],self.pos[1], self.text)
        painter.drawText(self.pos[0],self.pos[1]+300, "Test")
        painter.end()





class TitleAndIcones(qt.QWidget) :

    def __init__(self) :
        qt.QWidget.__init__(self)
        self._build()

    def _build(self) :

        self.layout=qt.QGridLayout()
        self.layout.setSpacing(0)
        self.layout.setMargin(0)

        self.label = None
        self.button =None
        self.label= MyLabel("cmH2O",-10.0, 40.0,[10,150])
        pal = qt.QPalette()
        pal.setColor(qt.QPalette.Background, qt.Qt.black)
        self.label.setAutoFillBackground(True)
        self.label.setPalette(pal)
        self.label.show()

        self.layout.addWidget(self.label,0,0)

        myimage = qt.QLabel()
        myimage.setFixedSize(qt.QPixmap("Icones/colorbar.png").size())
        #myimage.setScaledContents(True)
        
        self.layout.addWidget(myimage,0,1)
        pix = qt.QPixmap("Icones/colorbar.png")
        myimage.setPixmap(pix)
        self.labelMax = MyLabel("10.00",0.0, 20,[10,30])
        pal = qt.QPalette()
        pal.setColor(qt.QPalette.Background, qt.Qt.black)
        self.labelMax.setAutoFillBackground(True)
        self.labelMax.setPalette(pal)
        self.labelMax.show()
        self.layout.addWidget(self.labelMax,0,2)
        
        self.labelMin = MyLabel("0.00000000000000000000000000000",0.0, 100,[-20,-20])
        pal = qt.QPalette()
        pal.setColor(qt.QPalette.Background, qt.Qt.black)
        self.labelMin.setAutoFillBackground(True)
        self.labelMin.setPalette(pal)
        self.labelMin.show()
        self.layout.addWidget(self.labelMin,1,2)
        
        



        self.setLayout(self.layout)

class MyMainWindow(qt.QMainWindow) :
    def __init__(self, parent=None):
        qt.QMainWindow.__init__(self, parent)
        self.mainWidget = TitleAndIcones()
        
        self.mainWidget.setAutoFillBackground(True)
        
        
        self.setCentralWidget(self.mainWidget)
        self.setWindowTitle('Pini3_Alpha ')
        print 'HELLO' 

if __name__ == "__main__":


    app = qt.QApplication(["-display"])
    foo = MyMainWindow()
    foo.show()

    sys.exit(app.exec_())
