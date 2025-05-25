from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class WebBrowser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Web Browser")
        self.resize(1024, 768)

        ### UI elements

        self.main_layout = QVBoxLayout()
        self.nav_bar_layout = QHBoxLayout()

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL...")
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.history_btn = QPushButton("History")
        self.history_btn.setCheckable(True)
        self.history_btn.clicked.connect(self.show_history)

        self.back_btn = QPushButton("<-")
        self.back_btn.clicked.connect(self.go_back)

        self.forward_btn = QPushButton("->")
        self.forward_btn.clicked.connect(self.go_forward)

        self.go_btn = QPushButton("Go")
        self.go_btn.clicked.connect(self.navigate_to_url)

        self.nav_bar_layout.addWidget(self.history_btn)
        self.nav_bar_layout.addWidget(self.back_btn)
        self.nav_bar_layout.addWidget(self.forward_btn)
        self.nav_bar_layout.addWidget(self.url_bar)
        self.nav_bar_layout.addWidget(self.go_btn)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://duckduckgo.com"))
        self.browser.urlChanged.connect(self.update_url_bar)

        self.content_layout = QHBoxLayout()
        self.history_list = QListWidget()
        self.history_list.setVisible(False)

        #prepare layout
        self.content_layout.addWidget(self.history_list)
        self.content_layout.addWidget(self.browser)
        self.main_layout.addLayout(self.nav_bar_layout)
        self.main_layout.addLayout(self.content_layout)

        self.setLayout(self.main_layout)            #apply layout

    def navigate_to_url(self):
        url = self.url_bar.text().strip()
        if not url.startswith(("http")):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

    def update_url_bar(self, qurl):
        self.url_bar.setText(qurl.toString())

    def go_back(self):
        self.browser.back()

    def go_forward(self):
        self.browser.forward()

    def show_history(self, checked):
        # toggle visibility
        if checked:
            self.history_list.clear()
            for pages in self.browser.history().items():
                self.history_list.addItem(f"{pages.title()} — {pages.url().toString()}")
            self.history_list.setVisible(True)
        else:
            self.history_list.setVisible(False)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = WebBrowser()
    window.show()
    sys.exit(app.exec_())
