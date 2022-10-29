from tokenize import String
from PIL import Image
import pytesseract
import webbrowser
import tkinter as tk
from tkinter import filedialog   
pytesseract.pytesseract.tesseract_cmd = r"C:\自己的東西\eatgg\tesseract.exe"
Text = pytesseract.image_to_string(Image.open(filedialog.askopenfilename()),lang = "chi_tra+eng")
Text=Text.replace(" ","")
URL="https://www.google.com.hk/search?hl=chi&q="+Text
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new(URL)
