import sys
from PyQt5.QtWidgets import QApplication ,QWidget,QLabel,QHBoxLayout,QLayout,QPushButton,QVBoxLayout
from PyQt5.QtCore import Qt,QTimer,QTime

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time=QTime(0,0,0,0)
        self.time_label=QLabel("00:00:00",self)
        self.button1=QPushButton("Start",self)
        self.button2=QPushButton("Stop",self)
        self.button3=QPushButton("Reset",self)
        self.timer=QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.setGeometry(550,325,700,200)

        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.setLayout(vbox)

        hbox=QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        vbox.addLayout(hbox)

        self.setStyleSheet("""QPushButton{
                           font-size:50px;
                           font-family:Arial;
                           padding:10px}""")
        
        self.time_label.setStyleSheet("font-size:150px; color:#00ff00; background:black; border-radius:20px")
        self.button1.clicked.connect(self.start)
        self.button2.clicked.connect(self.stop)
        self.button3.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)
    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time=QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self,time):
        hours=time.hour()
        minutes=time.minute()
        seconds=time.second()
        miliseconds=time.msec()//10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{miliseconds:02}"
    
    def update_display(self):
        self.time=self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))
        
        

def main():
    app=QApplication(sys.argv)
    watch=Stopwatch()
    watch.show()
    sys.exit(app.exec_())

main()

