import webbrowser as wb


def webauto():
        chrome_path = '"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" %s'
        URLS = ("stackoverflow.com", "https://github.com/luasampaio", "gmail.com",
                "https://adb-2013197995950192.12.azuredatabricks.net/browse?o=2013197995950192", "youtube.com",
                "https://dev.azure.com/RDOr-Corp/IA")

        for url in URLS:
                print("Opening: " + url)
        wb.get(chrome_path).open(url)


webauto()
