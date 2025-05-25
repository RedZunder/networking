from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
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

        self.back_btn = QPushButton("<-")
        self.back_btn.clicked.connect(self.go_back)

        self.forward_btn = QPushButton("->")
        self.forward_btn.clicked.connect(self.go_forward)

        self.go_btn = QPushButton("Go")
        self.go_btn.clicked.connect(self.navigate_to_url)

        self.nav_bar_layout.addWidget(self.back_btn)
        self.nav_bar_layout.addWidget(self.forward_btn)
        self.nav_bar_layout.addWidget(self.url_bar)
        self.nav_bar_layout.addWidget(self.go_btn)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://duckduckgo.com"))
        self.browser.urlChanged.connect(self.update_url_bar)

        self.main_layout.addLayout(self.nav_bar_layout)
        self.main_layout.addWidget(self.browser)
        self.setLayout(self.main_layout)

    def navigate_to_url(self):
        url = self.url_bar.text().strip()
        if not url.startswith(("http://")):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

    def update_url_bar(self, qurl):
        self.url_bar.setText(qurl.toString())

    def go_back(self):
        self.browser.back()

    def go_forward(self):
        self.browser.forward()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = WebBrowser()
    window.show()
    sys.exit(app.exec_())
