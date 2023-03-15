# How do I use Python to open up a webpage?

import webbrowser

url = 'https://bylinetimes.com/'

chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(url)



