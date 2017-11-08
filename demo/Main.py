# -*- coding: utf-8 -*-
'''
Created on 2017年11月3日

@author: Jeff Yang
'''
import SetWallpaper as sw
import Spider as sp

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QGridLayout, QWidget, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

class Bing(QMainWindow):
     
    def __init__(self):
        super().__init__()
        self.initUI()
         
    def initUI(self):
        self.setGeometry(400, 200, 500, 325)
        self.setFixedSize(self.width(), self.height());    
        self.setWindowTitle('Bing Wallpaper')
        self.setWindowIcon(QIcon('Bing.ico'))
        self.add_position_layout()
    
    # 添加布局部件
    def add_position_layout(self):
        
        bg_label = QLabel(self)  
        bg_label.resize(self.width(), self.height())
        bg_label.setScaledContents(True)
        
        def set_background_image(img):
            photo = QtGui.QPixmap()
            photo.loadFromData(img)
            bg_label.setPixmap(photo)
        
#         img = time.strftime("%Y%m%d") + '.jpg'
        img, self.filename = sp.show_img(sp.get_url())
        set_background_image(img)
        
        
#         label_1 = QLabel("<p style='font-size:25px;text-align:center;'><b>Path:</b></p>", self)
        label_1 = QLabel("     保存目录: ", self)
        label_1.setStyleSheet("QLabel{background:rgb(255,255,255,100)}")
        
        label_2 = QLabel("公众号：麻瓜码农", self)
        label_2.setStyleSheet("QLabel{background:rgb(255,255,255,100)}")
        label_2.move(400,300)
        
        path_edit = QLineEdit()
        path_edit.setText('D:/wallpaper')
        path_edit.setToolTip('抱歉！暂时不支持更换路径！')
        path_edit.setReadOnly(True)
        
        
#         def btn_change():
#             filename = QFileDialog.getExistingDirectory(self, directory=path_edit.text())
#             path_edit.setText(filename)
        
        self.day = 0
        
        def btn_previous(day):
            img, self.filename = sp.show_img(sp.get_url(self.day + 1))
            set_background_image(img)
            self.day += 1
            print(self.day)
        
        def btn_next(day):
            if self.day > 0:
                img, self.filename = sp.show_img(sp.get_url(self.day - 1))
                set_background_image(img)
                self.day -= 1
                print(self.day)
            else:
                QMessageBox.information(self, " ", "明天的壁纸还未更新哦！") 
        
        def btn_save(day):
            img = sp.get_img(sp.get_url(self.day))
            
        def btn_set_wallpaper(day):
            flag = sw.set_wallpaper('D:/wallpaper/' + self.filename)
            if not flag:
                QMessageBox.information(self, " ", "请先保存此壁纸!") 
        
#         button_1 = QPushButton("更改路径", self)
#         button_1.clicked.connect(btn_change)
        button_2 = QPushButton("前一张", self)
        button_2.setToolTip('查看前一天的必应图片！')
        button_2.clicked.connect(btn_previous)
        button_3 = QPushButton("设为壁纸", self)
        button_3.setToolTip('设置壁纸要先保存哦！')
        button_3.clicked.connect(btn_set_wallpaper)
        button_4 = QPushButton("保存", self)
        button_4.setToolTip('保存在该目录下！')
        button_4.clicked.connect(btn_save)
        button_5 = QPushButton("后一张", self)
        button_5.setToolTip('查看后一天的必应图片！')
        button_5.clicked.connect(btn_next)
        
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(label_1, 2, 0)
        grid.addWidget(path_edit, 2, 1, 1, 2)
#         grid.addWidget(button_1, 2, 3)
        
        grid.addWidget(button_2, 3, 0)
        grid.addWidget(button_3, 3, 1, 1, 2)
        grid.addWidget(button_4, 2, 3)
        grid.addWidget(button_5, 3, 3)
#         grid.addWidget(label_2)
        
        grid.setAlignment(Qt.AlignTop)
        
        layout_widget = QWidget()
        layout_widget.setLayout(grid)

        self.setCentralWidget(layout_widget)

        
if __name__ == '__main__':
    sp.get_img(sp.get_url())
    
    app = QApplication(sys.argv)
    bing = Bing()
    bing.show()
    sys.exit(app.exec_()) 
    
