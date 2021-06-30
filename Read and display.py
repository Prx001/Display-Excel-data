import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QGridLayout, QVBoxLayout, QFileDialog, QDesktopWidget
from pathlib import Path
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
		# dataTable.setRowCount(4)
		# dataTable.setColumnCount(4)
		# dataTable.setVerticalHeaderItem(0, QTableWidgetItem("Row 1"))
		# dataTable.setVerticalHeaderItem(1, QTableWidgetItem("Row 2"))
		# dataTable.setVerticalHeaderItem(2, QTableWidgetItem("Row 3"))
		# dataTable.setVerticalHeaderItem(3, QTableWidgetItem("Row 4"))
		# dataTable.setHorizontalHeaderItem(0, QTableWidgetItem("Column 1"))
		# dataTable.setHorizontalHeaderItem(1, QTableWidgetItem("Column 2"))
		# dataTable.setHorizontalHeaderItem(2, QTableWidgetItem("Column 3"))
		# dataTable.setHorizontalHeaderItem(3, QTableWidgetItem("Column 4"))
		# dataTable.setItem(0, 0, QTableWidgetItem("11"))
		# dataTable.setItem(0, 1, QTableWidgetItem("12"))
		# dataTable.setItem(0, 2, QTableWidgetItem("13"))
		# dataTable.setItem(0, 3, QTableWidgetItem("14"))
		# dataTable.setItem(1, 0, QTableWidgetItem("21"))
		# dataTable.setItem(1, 1, QTableWidgetItem("22"))
		# dataTable.setItem(1, 2, QTableWidgetItem("23"))
		# dataTable.setItem(1, 3, QTableWidgetItem("24"))
		# dataTable.setItem(2, 0, QTableWidgetItem("31"))
		# dataTable.setItem(2, 1, QTableWidgetItem("32"))
		# dataTable.setItem(2, 2, QTableWidgetItem("33"))
		# dataTable.setItem(2, 3, QTableWidgetItem("34"))
		# dataTable.setItem(3, 0, QTableWidgetItem("41"))
		# dataTable.setItem(3, 1, QTableWidgetItem("42"))
		# dataTable.setItem(3, 2, QTableWidgetItem("43"))
		# dataTable.setItem(3, 3, QTableWidgetItem("44"))
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
			excelContent = openpyxl.load_workbook(FILE_DIR)
			excelContent = excelContent.active
			self.ROWS = excelContent.max_row
			self.COLUMNS = excelContent.max_column
			self.setTable(self.ROWS, self.COLUMNS)
			for i in range(1, self.ROWS+1):
				row = excelContent.cell(i, 1)
				self.rows_list.append(row.value)
			for i in range(1, self.COLUMNS+1):
				col = excelContent.cell(1, i)
				self.columns_list.append(col.value)
			self.setTableContent()
			self.fileNameLabel.setText(str(FILE_DIR[::-1][:FILE_DIR[::-1].index("/"):][::-1]))
	def setTable(self, rows, columns):
		self.dataTable.setRowCount(int(rows))
		self.dataTable.setColumnCount(int(columns))
	def setTableContent(self):
		self.dataTable.setVerticalHeaderLabels(self.rows_list)
		self.dataTable.setHorizontalHeaderLabels(self.columns_list)
	def moveToCenter(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())