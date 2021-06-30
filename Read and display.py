import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QLabel, QTableWidget, QTableWidgetItem, QGridLayout, QFileDialog, QDesktopWidget
from pathlib import Path
import string
import openpyxl
class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.resize(800, 600)
		self.moveToCenter()
		self.setWindowTitle("Data display")
		grid = QGridLayout()
		self.dataTable = QTableWidget(self)
		self.ROWS = 0
		self.COLUMNS = 0
		self.rows_list = []
		self.columns_list = []
		self.excelContent = None
		chooseFileButton = QPushButton("Choose file", self)
		chooseFileButton.clicked.connect(self.chooseFile)
		self.fileNameLabel = QLabel("File name", self)
		grid.addWidget(self.dataTable, 1, 3, 1, 1)
		grid.addWidget(chooseFileButton, 2, 2, 1, 1)
		grid.addWidget(self.fileNameLabel, 0, 3, 1, 1)
		self.setLayout(grid)
		self.show()
	def chooseFile(self):
		user = str(Path.home()).removeprefix("C:\\Users\\")
		filename = QFileDialog.getOpenFileName(self, "Choose a file to read data from", f"C:\\Users\\{user}", "*.xlsx")
		if filename[0]:
			FILE_DIR = filename[0]
			self.excelContent = openpyxl.load_workbook(FILE_DIR)
			self.excelContent = self.excelContent.active
			self.ROWS = self.excelContent.max_row
			self.COLUMNS = self.excelContent.max_column
			self.setTableCounts()
			self.setTableContent()
			self.fileNameLabel.setText(str(FILE_DIR[::-1][:FILE_DIR[::-1].index("/"):][::-1]))
	def setTableCounts(self):
		self.dataTable.setRowCount(self.ROWS)
		self.dataTable.setColumnCount(self.COLUMNS)
	def setTableContent(self):
		self.dataTable.setVerticalHeaderLabels([str(i) for i in range(1, self.ROWS+1)])
		self.dataTable.setHorizontalHeaderLabels([str(i) for i in string.ascii_uppercase])
		self.fillTableCells()
	def fillTableCells(self):
		for j in range(1, self.COLUMNS + 1):
			for i in range(1, self.ROWS + 1):
				cell = self.excelContent.cell(i, j)
				self.dataTable.setItem(i - 1, j - 1, QTableWidgetItem(str(cell.value)))
	def moveToCenter(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())