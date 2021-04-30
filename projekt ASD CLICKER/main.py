from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes
from PyQt5.QtCore import QTimer

money = 0
click_amount = 1
minus_money = 20
minus_money_emp = 100
minus_money_hd = 1000
minus_money_CC = 5000
minus_money_dev = 50000
idle_money = 0


class Ui_ASDClicker(object):
    def setupUi(self, ASDClicker):
        # UI playable window
        ASDClicker.setObjectName("ASDClicker")
        ASDClicker.resize(800, 600)
        ASDClicker.setMaximumSize(800, 600)
        ASDClicker.setMinimumSize(800, 600)
        ASDClicker.setStyleSheet("background-color: #29b6f6;")
        # your current click ratio
        self.c_per_click = QtWidgets.QLabel(ASDClicker)
        self.c_per_click.setGeometry(QtCore.QRect(0, 450, 400, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.c_per_click.setFont(font)
        self.c_per_click.setObjectName("cpc")
        # your current money per second ratio
        self.mps = QtWidgets.QLabel(ASDClicker)
        self.mps.setGeometry(QtCore.QRect(0, 500, 600, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.mps.setFont(font)
        self.mps.setObjectName("mps")
        # cost of clicks +1
        self.counter_2 = QtWidgets.QLabel(ASDClicker)
        self.counter_2.setGeometry(QtCore.QRect(650, 30, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.counter_2.setFont(font)
        self.counter_2.setObjectName("counter_2")
        # buy clicks +1
        self.click = QtWidgets.QPushButton(ASDClicker)
        self.click.setGeometry(QtCore.QRect(650, 50, 100, 23))
        self.click.setObjectName("click")
        # cost of employee
        self.counter_3 = QtWidgets.QLabel(ASDClicker)
        self.counter_3.setGeometry(QtCore.QRect(650, 110, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.counter_3.setFont(font)
        self.counter_3.setObjectName("counter_3")
        # buy employee button
        self.empl = QtWidgets.QPushButton(ASDClicker)
        self.empl.setGeometry(QtCore.QRect(650, 130, 100, 23))
        self.empl.setObjectName("empl")
        # cost of HD
        self.hd_counter = QtWidgets.QLabel(ASDClicker)
        self.hd_counter.setGeometry(QtCore.QRect(650, 190, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.hd_counter.setFont(font)
        self.hd_counter.setObjectName("hd_counter")
        # buy HD button
        self.hd = QtWidgets.QPushButton(ASDClicker)
        self.hd.setGeometry(QtCore.QRect(650, 210, 100, 23))
        self.hd.setObjectName("hd")
        # cost of CC
        self.CC_counter = QtWidgets.QLabel(ASDClicker)
        self.CC_counter.setGeometry(QtCore.QRect(650, 270, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CC_counter.setFont(font)
        self.CC_counter.setObjectName("CC_counter")
        # buy CC button
        self.CC = QtWidgets.QPushButton(ASDClicker)
        self.CC.setGeometry(QtCore.QRect(650, 290, 100, 23))
        self.CC.setObjectName("CC")
        # cost of dev
        self.dev_counter = QtWidgets.QLabel(ASDClicker)
        self.dev_counter.setGeometry(QtCore.QRect(650, 350, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dev_counter.setFont(font)
        self.dev_counter.setObjectName("dev_counter")
        # buy dev button
        self.dev = QtWidgets.QPushButton(ASDClicker)
        self.dev.setGeometry(QtCore.QRect(650, 370, 100, 23))
        self.dev.setObjectName("dev")
        # money earned text
        self.counter = QtWidgets.QLabel(ASDClicker)
        self.counter.setGeometry(QtCore.QRect(0, 550, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.counter.setFont(font)
        self.counter.setObjectName("counter")
        # machine picture
        self.automat = QtWidgets.QLabel(ASDClicker)
        self.automat.setGeometry(QtCore.QRect(300, 110, 181, 221))
        self.automat.setText("")
        self.automat.setPixmap(QtGui.QPixmap("medium-2_25.png"))
        self.automat.setObjectName("automat")
        # button under the machine
        self.click_automat = QtWidgets.QPushButton(ASDClicker)
        self.click_automat.setEnabled(True)
        self.click_automat.setGeometry(QtCore.QRect(300, 100, 211, 221))
        self.click_automat.setAutoRepeat(False)
        self.click_automat.setObjectName("click_automat")
        # money counter
        self.money = QtWidgets.QLabel(ASDClicker)
        self.money.setGeometry(QtCore.QRect(240, 550, 551, 31))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.money.setFont(font)
        self.money.setObjectName("money")
        # save button
        self.save = QtWidgets.QPushButton(ASDClicker)
        self.save.setGeometry(QtCore.QRect(0, 20, 75, 23))
        self.save.setObjectName("save")
        # load button
        self.load = QtWidgets.QPushButton(ASDClicker)
        self.load.setGeometry(QtCore.QRect(0, 60, 75, 23))
        self.load.setObjectName("load")
        # connecting qt widgets to python functions
        self.click_automat.setStyleSheet("background: transparent")
        self.retranslateUi(ASDClicker)
        QtCore.QMetaObject.connectSlotsByName(ASDClicker)
        self.click_automat.clicked.connect(self.clicked)
        self.click.clicked.connect(self.add_clicks)
        self.empl.clicked.connect(self.employee)
        self.hd.clicked.connect(self.helpdesk)
        self.CC.clicked.connect(self.call_center)
        self.dev.clicked.connect(self.dev_team)
        self.save.clicked.connect(self.savegame)
        self.load.clicked.connect(self.loadgame)
        # update money every second by what you bought
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_emp_money)
        self.timer.start(1000)
        # fonts and other stylesheets
        self.save.setStyleSheet("background-color: #0077c2;\n" "color: white;\n" "  border-radius:5px;")
        self.load.setStyleSheet("background-color: #0077c2;\n" "color: white;\n" "  border-radius:5px;")
        self.click.setStyleSheet("background-color: #0077c2;\n" "color: white;\n" "  border-radius:5px;")
        self.empl.setStyleSheet("background-color: #0086c3;\n" "color: white;\n" "  border-radius:5px;")
        self.hd.setStyleSheet("background-color: #0086c3;\n" "color: white;\n" "  border-radius:5px;")
        self.CC.setStyleSheet("background-color: #0086c3;\n" "color: white;\n" "  border-radius:5px;")
        self.dev.setStyleSheet("background-color: #0086c3;\n" "color: white;\n" "  border-radius:5px;")

    def retranslateUi(self, ASDClicker):
        _translate = QtCore.QCoreApplication.translate
        ASDClicker.setWindowTitle(_translate("ASDClicker", "Dialog"))
        self.click.setText(_translate("ASDClicker", "Click +1"))
        self.empl.setText(_translate("ASDClicker", "Employee +1"))
        self.hd.setText(_translate("ASDClicker", "Helpdesk +1"))
        self.CC.setText(_translate("ASDClicker", "Call Center +1"))
        self.dev.setText(_translate("ASDClicker", "Developer +1"))
        self.counter.setText(_translate("ASDClicker", "Currently earned :"))
        self.money.setText(_translate("ASDClicker", "0 $"))
        self.c_per_click.setText(_translate("ASDClicker", "Click Ratio: X1"))
        self.mps.setText(_translate("ASDClicker", "Money per second : 0 $"))
        self.counter_2.setText(_translate("ASDClicker",
                                          "<html><head/><body><p><span style=\" font-size:8pt;\">COST : 20 $</span></p></body></html>"))
        self.counter_3.setText(_translate("ASDClicker",
                                          "<html><head/><body><p><span style=\" font-size:8pt;\">COST : 100 $</span></p></body></html>"))
        self.hd_counter.setText(_translate("ASDClicker",
                                           "<html><head/><body><p><span style=\" font-size:8pt;\">COST : 1000 $</span></p></body></html>"))
        self.CC_counter.setText(_translate("ASDClicker",
                                           "<html><head/><body><p><span style=\" font-size:8pt;\">COST : 5000 $</span></p></body></html>"))
        self.dev_counter.setText(_translate("ASDClicker",
                                            "<html><head/><body><p><span style=\" font-size:8pt;\">COST : 50000 $</span></p></body></html>"))
        self.save.setText(_translate("ASDClicker", "Save game !"))
        self.load.setText(_translate("ASDClicker", "Load game !"))
        self.click_automat.setText(_translate("ASDClicker", ""))

    # DISPLAY UPDATED MONEY
    def update_emp_money(self):
        global money
        money = money + idle_money
        self.money.setText(f"{money} $")

    # clicks gives you money function
    def clicked(self):
        global money
        money += click_amount
        self.money.setText(f"{money} $")

    def add_clicks(self):
        global money
        global click_amount
        global minus_money
        if money >= minus_money:
            money -= minus_money
            self.money.setText(f"{money} $")
            click_amount += 1
            self.c_per_click.setText(f"Click Ratio: X{click_amount}")
            minus_money = minus_money * 2
            self.counter_2.setText(
                f"<html><head/><body><p><span style=\" font-size:8pt;\">COST : {minus_money} $</span></p></body></html>")
        else:
            ctypes.windll.user32.MessageBoxW(0, 'Masz za mało środków', "Wystąpił błąd", 0x10)

    def employee(self):
        global money
        global minus_money_emp
        global idle_money
        if money >= minus_money_emp:
            money -= minus_money_emp
            self.money.setText(f"{money} $")
            minus_money_emp = minus_money_emp * 2
            self.counter_3.setText(
                f"<html><head/><body><p><span style=\" font-size:8pt;\">COST : {minus_money_emp} $</span></p></body></html>")
            idle_money += 1
            self.mps.setText(f"Money per second:{idle_money} $")
        else:
            ctypes.windll.user32.MessageBoxW(0, 'Masz za mało środków', "Wystąpił błąd", 0x10)

    def helpdesk(self):
        global money
        global minus_money_emp
        global idle_money
        global minus_money_hd
        if money >= minus_money_hd:
            money -= minus_money_hd
            self.money.setText(f"{money} $")
            minus_money_hd = minus_money_hd * 3
            self.hd_counter.setText(
                f"<html><head/><body><p><span style=\" font-size:8pt;\">COST : {minus_money_hd} $</span></p></body></html>")
            idle_money += 10
            self.mps.setText(f"Money per second:{idle_money} $")
        else:
            ctypes.windll.user32.MessageBoxW(0, 'Masz za mało środków', "Wystąpił błąd", 0x10)

    def call_center(self):
        global money
        global idle_money
        global minus_money_CC
        if money >= minus_money_CC:
            money -= minus_money_CC
            self.money.setText(f"{money} $")
            minus_money_CC = minus_money_CC * 3
            self.CC_counter.setText(
                f"<html><head/><body><p><span style=\" font-size:8pt;\">COST : {minus_money_CC} $</span></p></body></html>")
            idle_money += 50
            self.mps.setText(f"Money per second:{idle_money} $")
        else:
            ctypes.windll.user32.MessageBoxW(0, 'Masz za mało środków', "Wystąpił błąd", 0x10)

    def dev_team(self):
        global money
        global idle_money
        global minus_money_dev
        if money >= minus_money_dev:
            money -= minus_money_dev
            self.money.setText(f"{money} $")
            minus_money_dev = minus_money_dev * 5
            self.dev_counter.setText(
                f"<html><head/><body><p><span style=\" font-size:8pt;\">COST : {minus_money_dev} $</span></p></body></html>")
            idle_money += 10000
            self.mps.setText(f"Money per second:{idle_money} $")
        else:
            ctypes.windll.user32.MessageBoxW(0, 'Masz za mało środków', "Wystąpił błąd", 0x10)

    def savegame(self):
        f = open('save.py', 'w')
        f.write(str(money) + "\n")
        f.write(str(minus_money) + "\n")
        f.write(str(click_amount) + "\n")
        f.write(str(minus_money_emp) + "\n")
        f.write(str(idle_money) + "\n")
        f.write(str(minus_money_hd) + "\n")
        f.write(str(minus_money_CC) + "\n")
        f.write(str(minus_money_dev) + "\n")
        f.close()
        ctypes.windll.user32.MessageBoxW(0, 'Game Saved !', "Save", 0x40)

    def loadgame(self):
        global money
        global minus_money
        global click_amount
        global idle_money
        global minus_money_emp
        global minus_money_hd
        global minus_money_CC
        global minus_money_dev
        f = open("save.py", "r")
        load_money = f.readline()
        load_moneymin = f.readline()
        load_click = f.readline()
        load_emp = f.readline()
        load_idle = f.readline()
        load_minus_hd = f.readline()
        load_minus_CC = f.readline()
        load_minus_dev = f.readline()
        money = (int(load_money))
        self.money.setText(f"{money} $")
        minus_money = (int(load_moneymin))
        self.counter_2.setText(
            f"<html><head/><body><p><span style=\" font-size:8pt;\">COST : {minus_money} $</span></p></body></html>")
        click_amount = (int(load_click))
        self.c_per_click.setText(f"Click Ratio: X{click_amount}")
        minus_money_emp = (int(load_emp))
        self.counter_3.setText(
            f"<html><head/><body><p><span style=\" font-size:8pt;\">COST : {minus_money_emp} $</span></p></body></html>")
        idle_money = (int(load_idle))
        self.mps.setText(f"Money per second: {idle_money} $")
        minus_money_hd = (int(load_minus_hd))
        self.hd_counter.setText(
            f"<html><head/><body><p><span style=\" font-size:8pt;\">COST : {minus_money_hd} $</span></p></body></html>")
        minus_money_CC = (int(load_minus_CC))
        self.CC_counter.setText(
            f"<html><head/><body><p><span style=\" font-size:8pt;\">COST : {minus_money_CC} $</span></p></body></html>")
        minus_money_dev = (int(load_minus_dev))
        self.dev_counter.setText(
            f"<html><head/><body><p><span style=\" font-size:8pt;\">COST : {minus_money_dev} $</span></p></body></html>")
        ctypes.windll.user32.MessageBoxW(0, 'Game Loaded !', "Load", 0x40)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ASDClicker()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
