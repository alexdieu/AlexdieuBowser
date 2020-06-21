from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import os
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pbar = QProgressBar()
        self.pbar.setMaximumWidth(120)

        self.browser=QWebEngineView(loadProgress=self.pbar.setValue, loadFinished=self.pbar.hide,
                                  loadStarted=self.pbar.show, titleChanged=self.setWindowTitle)
        self.browser.setUrl(QUrl("https://duckduckgo.com/"))
        self.setCentralWidget(self.browser)

        self.browser.page().linkHovered.connect(self.if_link_hover)
        
        self.browser.setMinimumSize(1200, 600)
        self.status = self.statusBar()
        self.status.addPermanentWidget(self.pbar)

        self.show()
        self.setWindowTitle("Alexdieu's Engine !")
        self.setWindowIcon(QIcon("AlexdieuIcon"))

        tb2 = QToolBar("Raccourcis :")
        tb2.setIconSize(QSize(45,45))
        self.addToolBar(Qt.RightToolBarArea,tb2)

        wiki_btn = QAction(QIcon("wiki.png"), "Wikipedia", self)
        wiki_btn.setStatusTip("Aller à Wikipédia - L'encyclopédie gratuite")
        wiki_btn.triggered.connect(lambda: self.conn("https://fr.wikipedia.org/wiki/Wikipédia:Accueil_principal"))
        tb2.addAction(wiki_btn)

        fb_btn = QAction(QIcon("facebook.png"), "Facebook", self)
        fb_btn.setStatusTip("Aller à Facebook (Tackage intersite attention !)")
        fb_btn.triggered.connect(lambda:self.conn("https://fr-fr.facebook.com/"))
        tb2.addAction(fb_btn)

        y_btn = QAction(QIcon("yahoo.png"), "Yahoo!", self)
        y_btn.setStatusTip("Aller à Yahoo")
        y_btn.triggered.connect(lambda: self.conn("https://fr.yahoo.com/"))
        tb2.addAction(y_btn)

        tw_btn = QAction(QIcon("twitter.png"), "Twitter", self)
        tw_btn.setStatusTip("Aller à twitter(Tackage intersite attention !)")
        tw_btn.triggered.connect(lambda: self.conn("http://www.twitter.com"))
        tb2.addAction(tw_btn)

        red_btn = QAction(QIcon("reddit.png"), "Reddit", self)
        red_btn.setStatusTip("Aller à reddit")
        red_btn.triggered.connect(lambda: self.conn("https://www.reddit.com/"))
        tb2.addAction(red_btn)

        ig_btn = QAction(QIcon("Instagram_icon.png"), "Instagram", self)
        ig_btn.setStatusTip("Aller sur Instagram")
        ig_btn.triggered.connect(lambda: self.conn("https://www.instagram.com/"))
        tb2.addAction(ig_btn)

        li_btn = QAction(QIcon("linkedin.png"), "Linkedin", self)
        li_btn.setStatusTip("Aller sur Linkedin")
        li_btn.triggered.connect(lambda: self.conn("https://linkedin.com"))
        tb2.addAction(li_btn)

        git_btn = QAction(QIcon("github.png"), "Github", self)
        git_btn.setStatusTip("Go to Github")
        git_btn.triggered.connect(lambda: self.conn("https://github.com"))
        tb2.addAction(git_btn)

        stack_btn = QAction(QIcon("stack.png"), "Stack Overflow", self)
        stack_btn.setStatusTip("Aller sur Stack Overflow(forum de devellopement)")
        stack_btn.triggered.connect(lambda: self.conn("https://stackoverflow.com"))
        tb2.addAction(stack_btn)

        p_btn = QAction(QIcon("pin.jpg"), "Pinterest", self)
        p_btn.setStatusTip("Aller sur Pinterest")
        p_btn.triggered.connect(lambda: self.conn("https://www.pinterest.fr/"))
        tb2.addAction(p_btn)

        am_btn = QAction(QIcon("amazon.png"), "Amazon", self)
        am_btn.setStatusTip("Aller sur Amazon")
        am_btn.triggered.connect(lambda: self.conn("https://www.amazon.fr/"))
        tb2.addAction(am_btn)

        eb_btn = QAction(QIcon("ebay.png"), "Ebay", self)
        eb_btn.setStatusTip("Aller sur Ebay")
        eb_btn.triggered.connect(lambda: self.conn("https://ebay.fr"))
        tb2.addAction(eb_btn)

        nx_btn = QAction(QIcon("netflix.png"), "Netflix", self)
        nx_btn.setStatusTip("Aller sur Netflix")
        nx_btn.triggered.connect(lambda: self.conn("https://www.netflix.com/fr/"))
        tb2.addAction(nx_btn)

        msn_btn = QAction(QIcon("msn.png"), "MSN", self)
        msn_btn.setStatusTip("Aller sur MSN")
        msn_btn.triggered.connect(lambda: self.conn("https://msn.com"))
        tb2.addAction(msn_btn)

        tb=QToolBar("Navigation")
        tb.setIconSize(QSize(25,25))
        self.addToolBar(tb)

        win_btn = QAction(QIcon("nouvfenetre"), "Nouvelle fenetre", self)
        win_btn.setStatusTip("Créer une nouvelle fenetre")
        win_btn.triggered.connect(self.new_win)
        tb.addAction(win_btn)

        tb.addSeparator()

        back_btn=QAction(QIcon("AV.png"),"Retour",self)
        back_btn.setStatusTip("Revenir sur la page d'avant")
        back_btn.triggered.connect(self.browser.back)
        tb.addAction(back_btn)


        fwd_btn = QAction(QIcon("AP.png"), "Après", self)
        fwd_btn.setStatusTip("Revenir sur la page d'après")
        fwd_btn.triggered.connect(self.browser.forward)
        tb.addAction(fwd_btn)

        home_btn = QAction(QIcon("home.png"), "Home", self)
        home_btn.setStatusTip("Go to home page")
        home_btn.triggered.connect(self.gohome)
        tb.addAction(home_btn)

        rld_btn = QAction(QIcon("recharge.png"), "Régénerer", self)
        rld_btn.setStatusTip("Recharger la page")
        rld_btn.triggered.connect(self.browser.reload)
        tb.addAction(rld_btn)

        self.urlbar=QLineEdit()
        tb.addSeparator()
        self.urlbar.returnPressed.connect(self.navigate_page)
        tb.addWidget(self.urlbar)

        self.browser.urlChanged.connect(self.update_url)

        stop_btn=QAction(QIcon("stop.png"),"Stop",self)
        stop_btn.setStatusTip("Arreter de charger la page")
        stop_btn.triggered.connect(self.browser.stop)
        tb.addAction(stop_btn)

        self.statusBar().showMessage('Navigateur d\'Alexdieu')
        self.show()

    def new_win(self):
        windo = MainWindow()
        windo.show()

    def update_url(self,q):
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

    def gohome(self):
        self.browser.setUrl(QUrl("https://duckduckgo.com/"))

    def navigate_page(self):
        q=QUrl(self.urlbar.text())
        t=self.urlbar.text()
        if "." not in t:
            t='https://duckduckgo.com/?q='+t
            self.browser.setUrl(QUrl(t))
        elif q.scheme()=="":
            q.setScheme("http")
            self.browser.setUrl(q)
        else:
            self.browser.setUrl(q)

    def conn(self,s):
        self.browser.setUrl(QUrl(s))

    def if_link_hover(self, l):
        self.status.showMessage(l)

app=QApplication(sys.argv)
window=MainWindow()
window.show()
sys.exit(app.exec())
