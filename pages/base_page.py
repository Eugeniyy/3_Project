#base_page - базовые классы и методы

class BasePage():
    
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

#Пустая строка!