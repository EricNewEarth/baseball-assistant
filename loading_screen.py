import time
import random
from tkinter import *
from PIL import Image, ImageTk

def build_loading_screen() -> Tk:

    # Create loading screen window
    loading_window = Tk()
    loading_window.title('Baseball Assistant')
    loading_window.geometry('200x200')
    window_width = 600
    window_height = 351
    screen_width = loading_window.winfo_screenwidth()
    screen_height = loading_window.winfo_screenheight()
    x_coord = (screen_width / 2) - (window_width / 2)
    y_coord = (screen_height / 2) - (window_height / 2)
    loading_window.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coord, y_coord))
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

def loading_animation(loading_window: Tk, animation1: PhotoImage, animation2: PhotoImage):
        
    random_text = splash_text()
    splash = Label(loading_window, text=random_text, fg = 'white', bg = '#272727')
    splash.configure(font = ('Calibri', 12))
    splash.place(relx = 0.5, y = 235, anchor = 'center')

    for _ in range(5):
        Label(loading_window, image=animation1, border=0, relief=SUNKEN).place(x=260, y=200)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=280, y=200)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=300, y=200)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=320, y=200)
        loading_window.update_idletasks()
        time.sleep(0.5)

        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=260, y=200)
        Label(loading_window, image=animation1, border=0, relief=SUNKEN).place(x=280, y=200)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=300, y=200)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=320, y=200)
        loading_window.update_idletasks()
        time.sleep(0.5)

        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=260, y=200)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=280, y=200)
        Label(loading_window, image=animation1, border=0, relief=SUNKEN).place(x=300, y=200)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=320, y=200)
        loading_window.update_idletasks()
        time.sleep(0.5)

        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=260, y=200)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=280, y=200)
        Label(loading_window, image=animation2, border=0, relief=SUNKEN).place(x=300, y=200)
        Label(loading_window, image=animation1, border=0, relief=SUNKEN).place(x=320, y=200)
        loading_window.update_idletasks()
        time.sleep(0.5)

def splash_text():

    splashes = [    
        'Closing the roof in Arizona...', # ARI
        'Failing to keep the A\'s in Oakland...', # ATH
        'Warming up The Freeze in Atlanta...', # ATL
        'Hydrating the Bird Bath Splash Zone in Baltimore...', # BAL
        'Taming the Green Monster...', # BOS
        'Keeping the Wrigley Field wind in check...', # CHC
        'Blacking out the White Sox park...', # CWS
        'Opening Day in the Queen City...', # CIN
        'Guarding the city of Cleveland...', # CLE
        'Trying to lower the altitude in Colorado...', # COL
        'Roaming the outfield in Comerica Park...', # DET
        'Fueling the train at Houston...', # HOU
        'Testing the fountains in Kansas City...', # KCR
        'Freeing Mike Trout from Anaheim...', # LAA
        'Cooking up the Dodger Dogs...', # LAD
        'Bringing WBC energy to Miami...', # MIA
        'Pouring the beer in Milwaukee...', # MIL
        'Touring the Twin Cities...', # MIN
        'Testing the home run Apple at Citi Field...', # NYM
        'Practicing the Yankee Stadium roll call...', # NYY
        'Ringing the bell in Philadelphia...', # PHI 
        'Admiring the view at PNC Park...', # PIT
        'Pulling out the bats in Slam Diego...', # SDP
        'Fishing the baseballs out of McCovey Cove...', # SFG
        'Practicing the Victory Dance in Seattle...', # SEA
        'Photographing the Gateway Arch...', # STL
        'Cleaning the devil ray tank in Tampa...', # TBR
        'Polishing the World Series rings in Arlington...', # TEX
        'Testing Toronto\'s home run horn...', # TOR
        'Traveling to our nation\'s capital...' # WSH
    ]
    
    random_text = random.randint(0, 29)
    return splashes[random_text]