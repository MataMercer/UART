from fbs_runtime.application_context import ApplicationContext
from PySide2.QtWidgets import QMainWindow
from PySide2 import QtCore, QtGui, QtWidgets
import sys, sqlite3, os, random


#Generated UI Code (Using the QtDesigner program to design the UI)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 376)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imageFoldersListWidget = QtWidgets.QListWidget(self.groupBox)
        self.imageFoldersListWidget.setObjectName("imageFoldersListWidget")
        self.horizontalLayout.addWidget(self.imageFoldersListWidget)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addNewFolderButton = QtWidgets.QPushButton(self.groupBox_3)
        self.addNewFolderButton.setObjectName("addNewFolderButton")
        self.verticalLayout_2.addWidget(self.addNewFolderButton)
        self.removeSelectedButton = QtWidgets.QPushButton(self.groupBox_3)
        self.removeSelectedButton.setObjectName("removeSelectedButton")
        self.verticalLayout_2.addWidget(self.removeSelectedButton)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.selectRandomFolderButton = QtWidgets.QPushButton(self.groupBox_2)
        self.selectRandomFolderButton.setObjectName("selectRandomFolderButton")
        self.verticalLayout_3.addWidget(self.selectRandomFolderButton)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.openRandomImageButton = QtWidgets.QPushButton(self.groupBox_4)
        self.openRandomImageButton.setObjectName("openRandomImageButton")
        self.horizontalLayout_3.addWidget(self.openRandomImageButton)
        self.verticalLayout.addWidget(self.groupBox_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 414, 21))
        self.menubar.setObjectName("menubar")
        self.menuUARRT = QtWidgets.QMenu(self.menubar)
        self.menuUARRT.setObjectName("menuUARRT")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionFolder_Path_List = QtWidgets.QAction(MainWindow)
        self.actionFolder_Path_List.setObjectName("actionFolder_Path_List")
        self.actionDefault_Profile = QtWidgets.QAction(MainWindow)
        self.actionDefault_Profile.setObjectName("actionDefault_Profile")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout_Ultimate_Art_Referencing_Tool = QtWidgets.QAction(MainWindow)
        self.actionAbout_Ultimate_Art_Referencing_Tool.setObjectName("actionAbout_Ultimate_Art_Referencing_Tool")
        self.menuUARRT.addAction(self.actionOpen)
        self.menuUARRT.addAction(self.actionSave)
        self.menuUARRT.addAction(self.actionSave_as)
        self.menuUARRT.addSeparator()
        self.menuUARRT.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionAbout_Ultimate_Art_Referencing_Tool)
        self.menubar.addAction(self.menuUARRT.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Ultimate Art Reference Tool", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Image Folders", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "Edit Folders", None, -1))
        self.addNewFolderButton.setText(QtWidgets.QApplication.translate("MainWindow", "Add New Folder", None, -1))
        self.removeSelectedButton.setText(QtWidgets.QApplication.translate("MainWindow", "Remove Selected", None, -1))
        self.selectRandomFolderButton.setText(QtWidgets.QApplication.translate("MainWindow", "Select Random Folder", None, -1))
        self.openRandomImageButton.setText(QtWidgets.QApplication.translate("MainWindow", "Open Random Image", None, -1))
        self.menuUARRT.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.menuAbout.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.actionFolder_Path_List.setText(QtWidgets.QApplication.translate("MainWindow", "Folder Path List", None, -1))
        self.actionDefault_Profile.setText(QtWidgets.QApplication.translate("MainWindow", "Default Profile", None, -1))
        self.actionOpen.setText(QtWidgets.QApplication.translate("MainWindow", "Open", None, -1))
        self.actionSave.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.actionSave_as.setText(QtWidgets.QApplication.translate("MainWindow", "Save as", None, -1))
        self.actionQuit.setText(QtWidgets.QApplication.translate("MainWindow", "Quit", None, -1))
        self.actionAbout_Ultimate_Art_Referencing_Tool.setText(QtWidgets.QApplication.translate("MainWindow", "About Ultimate Art Referencing Tool", None, -1))
#END Generated Code



class UserInterface(Ui_MainWindow):
    def __init__(self, mainwindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(mainwindow)
        self.connectButtons()   
        
        #use settings file in current directory. Creates new one if it doesn't exist.
        self.generalSettingsPath = 'settings'
        self.generalSettings = GeneralSettings(self.generalSettingsPath)

        #currentProfile path is set to the one specified in generalSettings. If none specified, leave it blank and assign it when the user saves.
        #This is so that the user can return where they left off from their previous session.
        try:
            self.currentProfilePath = self.generalSettings.getDefaultProfilePath()
        except:
            self.currentProfilePath = ''
        
        if self.currentProfilePath:
            self.openProfileFromPreviousSession()

        self.aboutInfo = '<b>Ultimate Art Reference Tool 0.0.1</b> <p>A program for choosing a reference easier.</p> '


    def connectButtons(self):
        self.addNewFolderButton.connect(QtCore.SIGNAL("clicked()"), self.addFolderPath)
        self.removeSelectedButton.connect(QtCore.SIGNAL("clicked()"), self.removeFolderPath)
        self.selectRandomFolderButton.connect(QtCore.SIGNAL("clicked()"), self.selectRandomFolder)
        self.openRandomImageButton.clicked.connect(self.openRandomImage)

        self.actionOpen.connect(QtCore.SIGNAL("triggered()"), self.openFile)
        self.actionSave.connect(QtCore.SIGNAL("triggered()"), self.save)
        self.actionSave_as.connect(QtCore.SIGNAL("triggered()"), self.saveAs)
        self.actionAbout_Ultimate_Art_Referencing_Tool.connect(QtCore.SIGNAL("triggered()"),self.informationMessage)
        self.centralwidget.connect(self.actionQuit, QtCore.SIGNAL("triggered()"),
                     QtWidgets.qApp, QtCore.SLOT("quit()"))

    '''[Button Functions Section (Functions that connect to the buttons directly.)]'''

    def addFolderPath(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, "Find Files", QtCore.QDir.currentPath()) 
        if directory:
            #check for duplicates
            dupeCheckSet = set(self.getAllStringsInWidgetList())
    
            if len(dupeCheckSet)>0 and directory in dupeCheckSet:
                return
            
            item = QtWidgets.QListWidgetItem(directory)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.imageFoldersListWidget.addItem(item)
    
    def removeFolderPath(self):
        self.imageFoldersListWidget.takeItem(self.imageFoldersListWidget.currentRow())


    def selectRandomFolder(self):
        #gather a list of paths that have a check mark. If there are none, do nothing
        listOfCheckedItems = [y[0] for y in list(filter(lambda x: x[1], self.getAllStringsAndCheckStateInWidgetList()))]
        if len(listOfCheckedItems)==0:
            return
        
        #avoid choosing the already selected item
        selectedItems = self.imageFoldersListWidget.selectedItems()
        
        doNotChooseIndex = -1
        if len(selectedItems)>0 and len(listOfCheckedItems)>1:
            doNotChooseIndex = self.imageFoldersListWidget.row(selectedItems[0])
        chosenItemIndex = 0
        if doNotChooseIndex == -1:
            chosenItemIndex = random.randint(0,len(listOfCheckedItems)-1)
        else:
            while True:
                chosenItemIndex = random.randint(0,len(listOfCheckedItems)-1)
                if chosenItemIndex != doNotChooseIndex:
                    break
        

        #select the randomly chosen item
        for i in range(0, self.imageFoldersListWidget.count()):
            if self.imageFoldersListWidget.item(i).text() == listOfCheckedItems[chosenItemIndex]:
                self.imageFoldersListWidget.item(i).setSelected(True)
                break


    def openRandomImage(self):
        selectedItems = self.imageFoldersListWidget.selectedItems()

        #list is empty; nothing to select.
        if self.imageFoldersListWidget.count()==0:
            return

        #check if nothing selected, then select one
        if len(selectedItems) == 0:
            self.selectRandomFolder()
            selectedItems = self.imageFoldersListWidget.selectedItems()

        try:
            selectedDirPath = selectedItems[0].text()
            listOfImageFilesInDir = self.getAllImagePathsInFolderRecursively(selectedDirPath)
            randomImagePath = os.path.join(selectedDirPath, random.choice(listOfImageFilesInDir))
            os.startfile(randomImagePath)
        except Exception as e:
            print(e)
            

    def openFile(self):
        fileName = (QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "Open File", QtCore.QDir.currentPath(),"*.db"))[0]
        if os.path.isfile(fileName):
            self.currentProfilePath = fileName
            profileSettings = ProfileSettings(self.currentProfilePath)
            self.loadIntoWidgetList(profileSettings)
            self.updateDefaultProfilePath()
            self.selectRandomFolder()


    def save(self):
        if not os.path.isfile(self.currentProfilePath):
            self.saveAs()
        else:
            profileSettings = ProfileSettings(self.currentProfilePath)
            profileSettings.clear()
            for x in self.getAllStringsAndCheckStateInWidgetList():
                profileSettings.addFolderPath(x[0], x[1])
            self.updateDefaultProfilePath()


    def saveAs(self):
        filePath = (QtWidgets.QFileDialog.getSaveFileName(self.centralwidget, "Find Files", QtCore.QDir.currentPath(),  "*.db"))[0]
        if filePath: 
            self.currentProfilePath = filePath
            profileSettings = ProfileSettings(self.currentProfilePath)
            for x in self.getAllStringsAndCheckStateInWidgetList():
                profileSettings.addFolderPath(x[0], x[1])
            self.updateDefaultProfilePath()


    def informationMessage(self):
        reply = QtWidgets.QMessageBox.information(self.centralwidget,
                "About Ultimate Art Reference Tool", self.aboutInfo)

    '''[UI Helper Utilities Section (functions that do not involve the UI directly)]'''
    
    def loadIntoWidgetList(self, profileSettings):
        self.imageFoldersListWidget.clear()
        listOfFolderTuples = profileSettings.getFolders()
        for x in listOfFolderTuples:
            item = QtWidgets.QListWidgetItem(x[0])
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            if x[1]:
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(QtCore.Qt.Unchecked)
            self.imageFoldersListWidget.addItem(item)


    def getAllStringsInWidgetList(self):
        folderList = []
        for i in range(0, self.imageFoldersListWidget.count()):
            item = self.imageFoldersListWidget.item(i)
            folderList.append(item.text())
        return folderList
    

    def getAllStringsAndCheckStateInWidgetList(self):
        folderList = []
        for i in range(0, self.imageFoldersListWidget.count()):
            item = self.imageFoldersListWidget.item(i)
            itemChecked = False
            if item.checkState():
                itemChecked = True
            folderList.append((item.text(), itemChecked))
        return folderList


    def fileNameIsImage(self, fileName):
        return fileName[-3:] =='png' or fileName[-3:] =='jpg' or fileName[-4:] =='jpeg' or fileName[-9:] == 'jpg_large' or fileName[-3:] =='tga'


    def getAllImagePathsInFolderRecursively(self, folderPath):
        listOfImageFiles = []
        #tail-end recursive helper function 
        def getAllImagePathsInFolderRecursively_helper(folderPath, listOfImageFiles):
            listOfAllFiles = os.listdir(folderPath)
            listOfImageFiles.extend([os.path.join(folderPath, fileName) for fileName in list(filter(lambda x: self.fileNameIsImage(x), listOfAllFiles))])
            for folder in list(filter(lambda x: os.path.isdir(os.path.join(folderPath, x)), listOfAllFiles)):  
                getAllImagePathsInFolderRecursively_helper(os.path.join(folderPath, folder), listOfImageFiles)
        
        getAllImagePathsInFolderRecursively_helper(folderPath, listOfImageFiles)
        return listOfImageFiles


    #defined for shorthand purposes
    def updateDefaultProfilePath(self):
        self.generalSettings.setDefaultProfilePath(self.currentProfilePath)


    def openProfileFromPreviousSession(self):
        if os.path.isfile(self.currentProfilePath):
            profileSettings = ProfileSettings(self.currentProfilePath)
            self.loadIntoWidgetList(profileSettings)
            self.selectRandomFolder()



class ProfileSettings:
    def __init__(self, profilePath):
        existsFlag = os.path.isfile(profilePath)

        db = sqlite3.connect(profilePath)
        self.db = db

        if not existsFlag:
            print('ProfileSettings: Connected to db [%s]' % profilePath)
            self.initDatabase()
            print('ProfileSettings: Initializing db [%s]' % profilePath)

            
    def initDatabase(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE folders(
                            path TEXT PRIMARY KEY, 
                            checked INTEGER)
        ''')
        self.db.commit()
        

    def getFolders(self):
        cursor = self.db.cursor()
        cursor.execute('''
            SELECT path, checked FROM folders
        ''')
        return cursor.fetchall()


    def addFolderPath(self, path, checked):
        cursor = self.db.cursor()
        cursor.execute('''INSERT OR REPLACE INTO folders(path, checked)
                  VALUES(?, ?)''', (path, int(checked)))
        self.db.commit()


    def clear(self):
        print('ProfileSettings: Clearing Database.')
        cursor = self.db.cursor()
        cursor.execute('''DROP TABLE folders''')
        self.initDatabase()



class GeneralSettings:
    def __init__(self, generalSettingsPath):
        existsFlag = os.path.isfile(generalSettingsPath)

        # # Create a database in RAM
        db = sqlite3.connect(generalSettingsPath)
        self.db = db

        if not existsFlag:
            self.initDatabase()
        

    def initDatabase(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE settings(
                            defaultProfilePath TEXT PRIMARY KEY 
                            )
        ''')
        self.db.commit()


    def getDefaultProfilePath(self):
        cursor = self.db.cursor()
        cursor.execute('''SELECT defaultProfilePath FROM settings''')
        return (cursor.fetchone())[0]


    def setDefaultProfilePath(self, defaultProfilePath):
        self.clear()
        cursor = self.db.cursor()
        cursor.execute('''INSERT INTO settings(defaultProfilePath)
                  VALUES(?)''', (defaultProfilePath,))
        self.db.commit()


    def clear(self):
        cursor = self.db.cursor()
        cursor.execute('''DROP TABLE settings''')
        self.initDatabase()



class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext
    def run(self):                              # 2. Implement run()
        # window = QMainWindow()
        # window.setWindowTitle("UltimateArtReferenceTool")
        # window.resize(250, 150)
        # window.show()

        mw = QMainWindow()
        ui = UserInterface(mw)
        mw.show()
        return self.app.exec_()                 # 3. End run() with this line

if __name__ == '__main__':
    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)