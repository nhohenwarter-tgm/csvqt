#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from view import Ui_CSVQt

import csv

class Controller(QMainWindow):
    """
    Controller
    Steuert den Ablauf
    """


    def __init__(self, parent=None):
        """
        Initialisiert das CSV-Tool
        """
        super().__init__(parent)
        self.view = Ui_CSVQt()
        self.view.setupUi(self)
        self.show()

    def read_file(self):
        """
        Liest einen Dateipfad von der GUI ein und gibt den Inhalt aus.
        """
        filepath = self.view.filepath.text()
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.view.output.setColumnCount(len(header))
            self.view.output.setHorizontalHeaderLabels(header)
            for row in reader:
                rowPosition = self.view.output.rowCount()
                self.view.output.insertRow(rowPosition)
                column = 0
                for item in row:
                    self.view.output.setItem(rowPosition, column, QTableWidgetItem(str(item)))
                    column += 1
