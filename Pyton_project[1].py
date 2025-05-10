# IMPORTS
import sys
import os
# PyQt5(PIP INSTALL PyQt5)
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# WEBENGINE(PIP INSTALL WEBENGINE)
from PyQt5.QtWebEngineWidgets import *
# MAINWINDOW
class MainWindow(QMainWindow):
    def __init__(self): #CONSTRCTOR FUNCTION
        super(MainWindow, self).__init__()

        # ADD WINDOW ELEMENTS
        # ADD TAB WIDGETS TO DISPLAY WEB TABS
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.setCentralWidget(self.tabs)
        # ADD DOUBLE CILCK EVENT LISTENER
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        # ADD TAB CLOSE EVENT LISTENER
        self.tabs.tabCloseRequested.connect(self.close_current_tabs)
         # ADD ACTIVE TAB CHANGED EVENT LISTENER
        self.tabs.currentChanged.connect(self.update_urlbar)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        # ADD NAVIGATION TOOLBAR
        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)
        # ADD BUTTONS TO NAVIGATION TOOLBAR
        # PERVIOUS WEB PAGE BUTTON
        back_btn = QAction(QIcon(os.path.join('icons', 'C:\\Users\\hadim\\Desktop\\icons\\icons8-back-button-30.png')), 'Back', self)
        back_btn.setStatusTip("Back to previous page")
        navtb.addAction(back_btn)
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())

        # NEXT WEB PAGE BUTTON
        next_btn = QAction(QIcon(os.path.join('icons', 'C:\\Users\\hadim\\Desktop\\icons\\icons8-forward-button-24.png')), 'Forward', self)
        next_btn.setStatusTip("Forward to previous page")
        navtb.addAction(next_btn)
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())

        # REFRESH WEB PAGE BUTTON
        reload_btn = QAction(QIcon(os.path.join('icons', 'C:\\Users\\hadim\\Desktop\\icons\\icons8-refresh-30.png')),  'Reload', self)
        reload_btn.setStatusTip("Reload page")
        navtb.addAction(reload_btn)
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())

        # HOME PAGE BUTTON
        home_btn = QAction(QIcon(os.path.join('icons', 'C:\\Users\\hadim\\Desktop\\icons\\icons8-home-button-24.png')), 'Home', self)
        home_btn.setStatusTip("Go home")
        navtb.addAction(home_btn)
        home_btn.triggered.connect(self.navigate_home)
        # ADD SEPARATOR TO NAVIGATION BUTTON
        navtb.addSeparator()   
        # ADD LABEL ICON TO SHOW THE SECURITY STATUS OF THE LOADED URL
        self.httpsicon = QLabel()
        self.httpsicon.setPixmap(QPixmap(os.path.join('icons', 'C:\\Users\\hadim\\Desktop\\icons\\icons8-bbc-50.png')))
        navtb.addWidget(self.httpsicon)
        #ADD LINE EDIT TO SHOW AND EDIT URLS
        self.urlbar = QLineEdit()
        navtb.addWidget(self.urlbar)
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        # ADD STOP TO STOP TGE URL LOADING
        stop_btn = QAction(QIcon(os.path.join('icons', 'C:\\Users\\hadim\\Desktop\\icons\\icons8-close-window-24.png')), 'Stop', self)
        stop_btn.setStatusTip("Stop loading current page")
        navtb.addAction(stop_btn)
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        # ADD TOP MENU
        # FILE MENU
        file_menu = self.menuBar().addMenu('&File')
        # ADD  FILE MENU ACTIONS
        new_tab_action = QAction(QIcon(os.path.join('icon', 'C:\\Users\\hadim\\Desktop\\icons\\icons8-stop-24.png')), 'New Tab', self)
        new_tab_action.setStatusTip('Open new tab')
        file_menu.addAction(new_tab_action)
        new_tab_action.triggered.connect(lambda _: self.add_new_tab())
        # HELP MENU
        help_menu = self.menuBar().addMenu('&Help')
        # ADD HELP MENU ACTIONS
        navigate_home_action = QAction(QIcon(os.path.join('icon', 'C:\\Users\\hadim\\Desktop\\icons\\icons8-help-24.png')), 'google', self)
        navigate_home_action.setStatusTip('Go to google')
        help_menu.addAction(navigate_home_action)
        navigate_home_action.triggered.connect(self.navigate_home)
        # ADD WINDOW TITLE AND ICON
        self.setWindowTitle('KAPPA BROWSER')
        self.setWindowIcon(QIcon(os.path.join('icons', 'C:\\Users\\hadim\\Desktop\\icons\\kappa.png')))
        # ADD STYLESHEET TO CUSTOMIZE YOUR WINDOW
        # STYLESHEET
        self.setStyleSheet("""QWidget{background-color: '#11DAFB'; color: rgb(0 , 0, 0);
        } QTabWidget::pane { /* The tab widget frame */ border-top: 2px solid rgb(15, 207, 245);
        position:absolute; top: -5em; top: -5em; color:rgb(0, 0, 0) padding: 5px;
        } QTabWidget::tab-bar {alignment: left; } /* Style the tab using the tab sub-control
        . Note that it reads QTabBar _not_ QTabWidget */ QLabel, QToolButton, QTabBar::tab {
        background: rgb(0, 0, 0); border: 2px solid rgb(90, 90 ,90); /*border-bottom-color:
        C2C7CB; /* same as the pane color */ min-width: 8ex; padding: 5px; margin-right: 2px;
         color: rgb(0, 0, 0); } QLabel:hover, QToolButton::hover, QTabBar::tab:selected, QTabBar::Tab:hover
        { background: rgb(0, 0, 0); border: 2px solid rgb(0, 36, 36); background-color: rgb(0, 0, 0); }
        QLineEdit { border: 2px solid rgb(0, 36, 36); border-radius: 10px; padding: 5px;
         background_color: rgb(0, 36, 36); color:rgb(0, 0, 0); }
        QLineEdit:hover { border: 2px solid rgb(0, 0, 0); } QLineEdit:focus{
         border: 2px solid rgb (0, 0, 0); color: rgb(0, 0, 0);}
        QPushButton{ background: rgb(0, 0, 0); border: 2px solid rgb(0, 0, 0); background-color: rgb(0, 0, 0); 
        padding: 5px; border-radius: 10px; page-background-color: rgb(0, 0, 0); }""")
        
        # LOAD DEFAULT HOME PAGE (GOOGLE.COM)
        # URL = https://www.bing.com
        # LABEL = HOMEPAGE
        self.add_new_tab(QUrl('https://www.bing.com'), "Homepage")
    #FUNCTIONS
    # ADD NEW WEB TAB
    def add_new_tab(self, qurl=None, label='Blank'):
                # CHECK IF URL VALUE IS BLANK
                if qurl is None:
                    qurl = QUrl('') # PASS EMPTY STRING TO URL
                # LOAD THE PASSED URL
                browser = QWebEngineView()
                browser.setUrl(qurl)
                # ADD THE WEB PAGE TAB 
                i = self.tabs.addTab(browser, label)
                self.tabs.setCurrentIndex(i)

                browser.urlChanged.connect(lambda qurl, borwser=browser:
                                        self.update_urlbar(qurl, borwser))
                browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                        self.tabs.setTabText(i, browser.page().title()))
                
                # SHOW MAIN WINDOW
                self.show() 
    # ADD NEW TAB ON DOUBLE CLICK ON TABS
    def tab_open_doubleclick(self, i):
            if i == -1: # NO TAB UNDER THE CILCK
                self.add_new_tab()
    # CLOSE TABS
    def close_current_tabs(self, i):
            if self.tabs.count() < 2: # ONLY CLOSE IF THERE IS MORE THAN ONE TAB OPEN
                return
            self.tabs.removeTab(i)
    # UPDATE URL TEXT WHEN ACTIVE TAB IS CHANGED        
    def update_urlbar(self, q, browser=None):
            if browser != self.tabs.currentWidget():
                  return
            if q.scheme() == "https":
                  self.httpsicon.setPixmap(QPixmap(os.path.join('icons', "icons8-bbc-50.png")))

            else:
                  self.httpsicon.setPixmap(QPixmap(os.path.join('icons', 'icons8-bbc-50.png')))
            self.urlbar.setText(q.toString())
            self.urlbar.setCursorPosition(0)
    # ACTIVE TAB CHANGED        
    def current_tab_changed(self, i):
            # i = TAB INDEX
            # GET CURRENT TAB URL
            qurl = self.tabs.currentWidget().url()
            # UPDATE URL TEXT
            self.update_urlbar(qurl, self.tabs.currentWidget())
            # UPDATE WINDOWS TITLE
            self.update_title(self.tabs.currentWidget())
    # UPDATE WINDOWS TITLE
    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            # IF THIS SIGNAL IS NOT FROM TEH CURRENT ACTIVE TAB, IGNORE
            return
        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle(title)
    # NAVIGATE TO PASSED URL
    def navigate_to_url(self): # DOSE NOT RECEIVE THE URL
        # GET URL TEXT 
        q = QUrl(self.urlbar.text()) 
        if q.scheme() == "":
              # PASS HTTP AS DEFAULT URL SCHEMA
              q.setScheme('http')
        self.tabs.currentWidget().setUrl(q)
    # NAVIGATE TO DEFAULT HOME PAGE    
    def navigate_home(self):
          self.tabs.currentWidget().setUrl(QUrl("http://bing.com"))
        
       


app = QApplication(sys.argv)
# APPLICATION NAME
app.setApplicationName("KAPPA BROWSER")


window = MainWindow()
app.exec_()
