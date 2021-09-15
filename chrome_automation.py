# Chrome Automation

import webbrowser as wb


def ChromeAutomation():
    chrome_path = "C:\Program Files\Google\Chrome\Application"
    urls = ("https://www.youtube.com/",
    "https://stackoverflow.com/", 
    "https://www.google.co.in/", 
    "https://drive.google.com/drive/u/0/my-drive", 
    "https://www.canva.com/",
    "https://coolors.co/",
    "https://apeescape.in/")

    for i in urls:
        print("Opening" + i)
        wb.get(chrome_path).open(i)


ChromeAutomation()

