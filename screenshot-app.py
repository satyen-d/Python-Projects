# Screenshot GUI Application

import time
import pyautogui as pyg
from tkinter import*

# Screenshot Function


def screenshot():
    # time.sleep(5)
    name = int(round(time.time()*1000))
    filename = "D:/python projects/Sarvesh Patil/Screenshots/{}.png".format(
        name)
    ss = pyg.screenshot(filename)
    ss.show()


# GUI Class
class ScreenshotApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Screenshot Application")
        self.window.configure(width=500, height=500)
        self.window.resizable(width=False, height=False)


        head_label = Label(self.window,
        text="Welcome", pady=10)
        head_label.place(relwidth=1)

        content_label = Label(self.window,
        text="This application is used for capturing screenshots.", pady=10)
        content_label.place(relwidth=1, rely=0.07, relheight=0.12)


        Ss_button = Button(self.window, text="Take Screenshot",
                           width=20, command=screenshot)
        Ss_button.place(relx=0.1, rely=0.3)

        quit_button = Button(self.window, text="Close", width=10, command=quit)
        quit_button.place(relx=0.7, rely=0.3)


if __name__ == "__main__":
    screenshott = ScreenshotApplication()
    screenshott.run()
