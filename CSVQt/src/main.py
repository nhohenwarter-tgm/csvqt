#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

from controller import Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller()
    sys.exit(app.exec_())
