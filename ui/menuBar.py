from PySide2.QtWidgets import QAction, QMessageBox

class MenuBar:
    def createMenuBar(self):
            menuBar = self.menuBar()
            fileOption = menuBar.addMenu("File")

            newAction = QAction("New", self)
            openAction = QAction("Open", self)
            saveAction = QAction("Save", self)
            saveAction.setShortcut('ctrl+s')
            saveAction.triggered.connect(self.saveApp)

            exitAction = QAction("Exit", self)
            exitAction.setShortcut('ctrl+w')
            exitAction.triggered.connect(self.exitApp)

            fileOption.addAction(newAction)
            fileOption.addAction(openAction)
            fileOption.addAction(saveAction)
            fileOption.addAction(exitAction)

    def exitApp(self):
        reply = self.createQuestionBox("Exit", "Are you sure you want to exit?")
        if reply:
            self.close()
        else:
            print("Exit cancelled.")

    def saveApp(self):
        self.createMessageBox("Save", "Saved successfully")

    def createQuestionBox(self, title, message):
        reply = QMessageBox.question(self, title, message,
                                    QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            print("Yes clicked.")
            return True
        else:
            print("No clicked.")
            return False


    def createMessageBox(self, title, message):
        reply = QMessageBox.about(self, title, message)