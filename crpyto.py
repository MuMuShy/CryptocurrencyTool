from CrpytoRequest import CoinCap
import time

from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
from PyQt5.QtWidgets import QWidget, QLineEdit, QListWidget, QPushButton,\
    QVBoxLayout, QLabel


class PriceThread(QThread):
    trigger = pyqtSignal(str)

    def __int__(self):
        # 初始化函数
        super(PriceThread, self).__init__()

    def init(self):
        self.data = CoinCap()

    def run(self):
        while True:
            print('price:')
            print(self.data.get_btc_price())
            time.sleep(5)

    def stop(self):
        self.terminate()