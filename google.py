import os
import subprocess


CHROME = os.path.join('C:\\', 'Program Files (x86)', 'Google', 'Chrome', 'Application', 'chrome.exe')

os.system('taskkill /im chrome.exe')
subprocess.call([CHROME, '--kiosk'])

# To open google chrome or google easily