import webbrowser

def firefox(url):
    webbrowser.register('firefox',
        None,
        webbrowser.BackgroundBrowser("/usr/bin/firefox"))
    webbrowser.get('firefox').open(url)