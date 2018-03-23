import sys

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QDoubleSpinBox, QPushButton,
    QVBoxLayout
)


class Converter(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUi()
        self.initLayouts()
        self.initSignals()
    def initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self)
        self.resultLabel = QLabel('Сумма в долларах', self)

        #self.testLabel = QLabel('тест', self)

        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(999999999)

        #self.testAmount = QDoubleSpinBox(self)
        #self.testAmount.setMaximum(999999999)

        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)
        #self.resultAmount.setReadOnly(True)

        self.convertBtn1 = QPushButton('р-->$', self)
        self.convertBtn2 = QPushButton('$-->p', self)
        self.clearBtn = QPushButton('Сбросить', self)



    def initSignals(self):
        self.convertBtn1.clicked.connect(self.onClickConvertBtn1)
        self.convertBtn2.clicked.connect(self.onClickConvertBtn2)
        self.srcAmount.valueChanged.connect(self.setButtonAvailability)
        self.resultAmount.valueChanged.connect(self.setButtonAvailability)
        self.clearBtn.clicked.connect(self.onClickClearBtn)


    def initLayouts(self):
        w = QWidget(self)

        self.mainLayout = QVBoxLayout(w)
        #self.mainLayout.addWidget(self.testLabel)
        #self.mainLayout.addWidget(self.testAmount)
        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertBtn1)
        self.mainLayout.addWidget(self.convertBtn2)
        self.mainLayout.addWidget(self.clearBtn)


        self.setCentralWidget(w)

    def onClickConvertBtn1(self):
        value = self.srcAmount.value()

        if value:
            self.resultAmount.setValue(value / 30)

    def onClickConvertBtn2(self):
        value = self.resultAmount.value()

        if value:
            self.srcAmount.setValue(value * 30)

    def onClickClearBtn(self):
        self.resultAmount.setValue(0)
        self.srcAmount.setValue(0)

    def setButtonAvailability(self):
        src_value = self.srcAmount.value()
        res_value = self.resultAmount.value()
        # check = src_value and res_value

        if src_value and res_value or not src_value and not res_value:
            self.convertBtn1.setDisabled(True)
            self.convertBtn2.setDisabled(True)
        elif src_value and not res_value:
            self.convertBtn1.setDisabled(False)
            self.convertBtn2.setDisabled(True)
        elif  not src_value and  res_value:
            self.convertBtn1.setDisabled(True)
            self.convertBtn2.setDisabled(False)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    c = Converter()
    c.show()

    sys.exit(app.exec_())
