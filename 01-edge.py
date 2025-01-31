## Abrindo paginas no edge 

import webbrowser as wb


def webauto():
        chrome_path = '"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" %s'
        URLS = ("stackoverflow.com", "https://github.com/luasampaio", "gmail.com",
               "youtube.com",
            

        for url in URLS:
                print("Opening: " + url)
        wb.get(chrome_path).open(url)


webauto()