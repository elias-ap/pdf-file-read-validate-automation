import os.path
import PyPDF2
import pytesseract
import selenium.webdriver as wb
import time
from pdf2image import convert_from_path
from selenium.webdriver.common.by import By

poppler_path = r'venv/Lib/site-packages/poppler-22.11.0/Library/bin'
global pdf_folder_path
global downloads_path

pdf_folder_path = os.path.abspath('Sources/PDF Files')
downloads_path = os.path.abspath('Sources/Downloads')

options = wb.ChromeOptions()
options.add_experimental_option('prefs', {
    "download.default_directory": downloads_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": False,
    "plugins.always_open_pdf_externally": True
})

browser = wb.Chrome(options=options)
browser.get(os.path.abspath("sources/HTML/download.html"))
browser.maximize_window()

candidate_list = browser.find_elements(By.XPATH, '/html/body/div/div/ul')
for candidate in candidate_list:
    certificates_list = candidate.find_elements(By.TAG_NAME, 'a')
    for certificate in certificates_list:
        certificate.click()
