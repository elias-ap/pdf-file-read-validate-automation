import time
import os as os
import selenium.webdriver
import PyPDF2
from selenium.webdriver.common.by import By

# SETTING OPTIONS FOR BROWSER
options = selenium.webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
"download.default_directory": "C:\\Users\\elias\\PycharmProjects\\python-pdf-file-read-validate-automation\downloads",
"download.prompt_for_download": False,
"download.directory_upgrade": False,
"plugins.always_open_pdf_externally": True
})

# OPEN BROWSER WITH SETTINGS DEFINIED
browser = selenium.webdriver.Chrome(options=options)
path = os.path.abspath("HTML/index.html")
browser.maximize_window()
browser.get(f"file:{path}")

# LOGIN SETTINGS
login = 'Elaine'
password = '123456'

# AUTOMATE LOGIN
login_label = browser.find_element(By.XPATH, '/html/body/div/div/div[1]/input')
password_label = browser.find_element(By.XPATH, '/html/body/div/div/div[2]/input')

time.sleep(1)
login_label.send_keys(login)
time.sleep(1)
password_label.send_keys(password)
time.sleep(1)
button_login = browser.find_element(By.XPATH, '/html/body/div/div/a/button')
button_login.click()
time.sleep(1)

# AUTOMATE DOWNLOAD
download_link = browser.find_element(By.XPATH, '/html/body/div/div/a')
download_link.click()

# GET DOWNLOADED FILE NAME
file_name = download_link.get_attribute('download')
time.sleep(2)

path = "C:\\Users\\elias\\PycharmProjects\\file-read-automation\downloads\\"

# OPEN PDF FILE AND GET TEXT IN PAGE ONE
pdf_file = open(f'{path}{file_name}', 'rb')
pdf_data = PyPDF2.PdfFileReader(pdf_file)
pdf_page = pdf_data.getPage(0)
text = pdf_page.extractText()

# TEXT VALIDATE
if text == 'TESTING PDF':
    print('Certificado válido')
else:
    print('Certificado inválido')





