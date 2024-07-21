from PySide2.QtWidgets import QAction, QMessageBox

# Menu bar mixin added to the main window class
class MenuBar:
    def createMenuBar(self):
            """
            This function creates and configures the menu bar for the main window.
            It adds a "File" menu with options for New, Save, and Exit.

            Parameters:
            self (MainWindow): The instance of the main window class. This parameter is required to access the QMainWindow and QAction classes.

            Returns:
            None: This function does not return any value. It modifies the menu bar of the main window.
            """
            # Get the menu bar from the MainWindow class. 
            # menuBar() method is a built-in method of the QMainWindow class
            menuBar = self.menuBar()

            # Adding a "File" menu to the menu bar
            fileOption = menuBar.addMenu("File")

            # Creating actions for "File" menu
            newAction = QAction("New", self)
            newAction.setShortcut('ctrl+n')
            # newAction.triggered.connect()

            saveAction = QAction("Save", self)
            saveAction.setShortcut('ctrl+s')
            saveAction.triggered.connect(self.saveApp)

            exitAction = QAction("Exit", self)
            exitAction.setShortcut('ctrl+w')
            exitAction.triggered.connect(self.exitApp)

            # Adding actions to the "File" menu
            fileOption.addAction(newAction)
            fileOption.addAction(saveAction)
            fileOption.addAction(exitAction)


    def exitApp(self):
        """
        This function displays a question box to confirm exiting the application.
        If the user confirms, it closes the application. Otherwise, it prints a message indicating cancellation.

        Parameters:
        self (MainWindow): The instance of the main window class.

        Returns:
        None
        """
        reply = self.createQuestionBox("Exit", "Are you sure you want to exit?")
        if reply:
            self.close()
        else:
            print("Exit cancelled.")

    def saveApp(self):
        """
        This function is responsible for initiating the save operation in the application.
        It displays a message box to confirm the save action. If the user confirms, it calls the
        createMessageBox function to display a success message.

        Parameters:
        self (MainWindow): The instance of the main window class.

        Returns:
        None
        """
        # Confirming save operation. May not be fully implemented :)
        self.createMessageBox("Save", "Saved successfully")

    def createQuestionBox(self, title, message):
        """
        This function creates a question box with the given title and message,
        offering the user a choice between Yes and No.

        Parameters:
        self (MainWindow): The instance of the main window class.
        title (str): The title of the question box.
        message (str): The message to be displayed in the question box.

        Returns:
        bool: True if the user clicks Yes, False if the user clicks No.
        """
        reply = QMessageBox.question(self, title, message,
                                    QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            print("Yes clicked.")
            return True
        else:
            print("No clicked.")
            return False


    def createMessageBox(self, title, message):
        """
        This function creates a generic message box with the given title and message.
        It uses the QMessageBox.about method from the PySide2.QtWidgets module.

        Parameters:
        self (MainWindow): The instance of the main window class. This parameter is required to access the QMessageBox class.
        title (str): The title of the message box. It should be a short and descriptive string.
        message (str): The message to be displayed in the message box. It can be a long string explaining the purpose or content.

        Returns:
        None: This function does not return any value. It only displays a message box.
        """
        reply = QMessageBox.about(self, title, message)