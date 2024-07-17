from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QAction, QMessageBox, QVBoxLayout, QWidget, QLineEdit, QPushButton
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python plotter")
        self.setGeometry(600, 200, 500, 500)
        self.setMinimumHeight(600)
        self.setMinimumWidth(900)

        self.createMenu()
        self.createMainLayout()

        self.show()

    def createMenu(self):
        menuBar = self.menuBar()
        fileOption = menuBar.addMenu("File")

        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        save_action.setShortcut('ctrl+s')
        save_action.triggered.connect(self.saveApp)

        exit_action = QAction("Exit", self)
        exit_action.setShortcut('ctrl+w')
        exit_action.triggered.connect(self.exitApp)

        fileOption.addAction(new_action)
        fileOption.addAction(open_action)
        fileOption.addAction(save_action)
        fileOption.addAction(exit_action)

    def exitApp(self):
        reply = self.createQuestionBox("Exit", "Are you sure you want to exit?")
        if reply:
            self.close()
        else:
            print("Exit cancelled.")
    

    def createQuestionBox(self, title, message):
        reply = QMessageBox.question(self, title, message,
                                    QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            print("Yes clicked.")
            return True
        else:
            print("No clicked.")
            return False

    def saveApp(self):
        self.createMessageBox("Save", "Saved successfully")


    def createMessageBox(self, title, message):
        reply = QMessageBox.about(self, title, message)
        
        
    def createMainLayout(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout(central_widget)
        
        self.createLeftSection(main_layout)
        
        plot_area = QWidget()
        plot_area.setStyleSheet("background-color: lightgray;")
        main_layout.addWidget(plot_area, stretch=5)

    def createLeftSection(self, main_layout):
        left_section = QWidget()
        left_section.setFixedWidth(300) 
        left_layout = QVBoxLayout(left_section)
        
        self.function_input = QLineEdit()
        self.function_input.setPlaceholderText("Enter function to plot")
        left_layout.addWidget(self.function_input)
        
        plot_button = QPushButton("Plot")
        plot_button.clicked.connect(self.plotFunction)
        left_layout.addWidget(plot_button)

        left_layout.addStretch()
        
        main_layout.addWidget(left_section)
    
    def plotFunction(self):
        function_text = self.function_input.text()
        print(f"Function to plot: {function_text}")



myApp = QApplication(sys.argv)
window = Window()

myApp.exec_()
sys.exit(0)