import sys
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout,QLabel
from PyQt5.QtCore import Qt,QTime,QTimer
from PyQt5.QtGui import QFont,QFontDatabase
class digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label=QLabel(self)
        self.setWindowTitle("Digital clock")
        self.timer=QTimer(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(600,350,700,150)
        self.setStyleSheet("background:black")
        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.setLayout(vbox)
        self.time_label.setStyleSheet("font-size:150px;"
                                      "color:#00ff00")
        
        font_id=QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family=QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font=QFont(font_family,150)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.Update_tiem)
        self.timer.start(1000)
        self.Update_tiem()
    def Update_tiem(self):
        current_time=QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


def main():
    app=QApplication(sys.argv)
    clock=digital_clock()
    clock.show()
    sys.exit(app.exec_())
main()