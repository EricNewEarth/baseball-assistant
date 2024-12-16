# Imports
from tkinter import *
from PIL import Image, ImageTk
import time
import random

def build_loading_screen():

    # Create loading screen window
    loading_window = Tk()
    loading_window.title("Baseball Assistant")
    loading_window.geometry("200x200")
    window_width = 600
    window_height = 351
    screen_width = loading_window.winfo_screenwidth()
    screen_height = loading_window.winfo_screenheight()
    x_coord = (screen_width / 2) - (window_width / 2)
    y_coord = (screen_height / 2) - (window_height / 2)
    loading_window.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))
    loading_window.overrideredirect(1) # Hides title bar

    Frame(loading_window, width = 600, height = 351, bg = '#272727').place(x=0, y=0)
    title_label = Label(loading_window, text = 'BASEBALL ASSISTANT', fg = 'white', bg = '#272727')
    title_label.configure(font = ('Anton', 48))
    title_label.place(x=50, y=90)

    loading_label = Label(loading_window, text = 'Loading...', fg = 'white', bg = '#272727')
    loading_label.configure(font = ('Calibri', 11))
    loading_label.place(x=10, y=320)

    loading_animation1 = ImageTk.PhotoImage(Image.open('images/c2.png'))
    loading_animation2 = ImageTk.PhotoImage(Image.open('images/c1.png'))

    loading_animation(loading_window, loading_animation1, loading_animation2)

    return loading_window

def loading_animation(loading_window, animation1, animation2):
        
    random_text = splash_text()
    splash = Label(loading_window, text=random_text, fg = 'white', bg = '#272727')
    splash.configure(font = ('Calibri', 12))
    splash.place(relx = 0.5, y = 235, anchor = 'center')

    for i in range(5):
        Label(loading_window, image=animation1, border=0, relief=SUNKEN).place(x=260, y=195)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=280, y=195)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=300, y=195)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=320, y=195)
        loading_window.update_idletasks()
        time.sleep(0.5)

        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=260, y=195)
        Label(loading_window, image=animation1, border=0, relief=SUNKEN).place(x=280, y=195)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=300, y=195)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=320, y=195)
        loading_window.update_idletasks()
        time.sleep(0.5)

        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=260, y=195)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=280, y=195)
        Label(loading_window, image=animation1, border=0, relief=SUNKEN).place(x=300, y=195)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=320, y=195)
        loading_window.update_idletasks()
        time.sleep(0.5)

        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=260, y=195)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=280, y=195)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=300, y=195)
        Label(loading_window, image=animation1, border=0, relief=SUNKEN).place(x=320, y=195)
        loading_window.update_idletasks()
        time.sleep(0.5)

def splash_text():
    text1 = 'Closing the roof in Arizona...' # ARI
    text2 = 'Warming up The Freeze in Atlanta...' # ATL
    text3 = 'Hydrating the Bird Bath Splash Zone in Baltimore...' # BAL
    text4 = 'Taming the Green Monster...' # BOS
    text5 = 'Keeping the Wrigley Field wind in check...' # CHC
    text6 = 'Blacking out the White Sox park...' # CWS
    text7 = 'Opening Day in the Queen City...' # CIN
    text8 = 'Guarding the city of Cleveland...' # CLE
    text9 = 'Trying to lower the altitude in Colorado...' # COL
    text10 = 'Roaming the outfield in Comerica Park...' # DET
    text11 = 'Fueling the train at Houston...' # HOU
    text12 = 'Testing the fountains in Kansas City...' # KCR
    text13 = 'Freeing Mike Trout from Anaheim...' # LAA
    text14 = 'Cooking up the Dodger Dogs...' # LAD
    text15 = 'Bringing WBC energy to Miami...' # MIA
    text16 = 'Pouring the beer in Milwaukee...' # MIL
    text17 = 'Touring the Twin Cities...' # MIN
    text18 = 'Testing the Citi Field home run Apple...' # NYM
    text19 = 'Practicing the Yankee Stadium roll call...' # NYY
    text20 = 'Trying to keep the A\'s in Oakland...' # OAK
    text21 = 'Ringing the bell in Philadelphia...' # PHI 
    text22 = 'Admiring the view at PNC Park...' # PIT
    text23 = 'Pulling out the bats in Slam Diego...' # SDP
    text24 = 'Fishing the baseballs out of McCovey Cove...' # SFG
    text25 = 'Practicing the Victory Dance in Seattle...' # SEA
    text26 = 'Photographing the Gateway Arch...' # STL
    text27 = 'Cleaning the devil ray tank in Tampa...' # TBR
    text28 = 'Polishing the World Series rings in Arlington...' # TEX
    text29 = 'Testing Toronto\'s home run horn...' # TOR
    text30 = 'Traveling to our nation\'s capital...' # WSH

    splashes = [text1, text2, text3, text4, text5, text6, text7, text8, text9, text10,
               text11, text12, text13, text14, text15, text16, text17, text18, text19, text20,
               text21, text22, text23, text24, text25, text26, text27, text28, text29, text30]
    
    random_text = random.randint(0, 29)
    return splashes[random_text]