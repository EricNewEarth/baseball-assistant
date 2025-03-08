import statsapi
import datetime
import schedule
import team_info
import logo_paths
import team_assets
import transactions
import injured_list
import tkinter as tk
from tkinter import *
from tkcalendar import Calendar

team_logos = logo_paths.logos

today = datetime.date.today()

def build_team_page(team):

    team_id = statsapi.lookup_team(team)[0]['id']
    assets = team_assets.return_assets(team)

    # Create the team page window
    main_window = tk.Toplevel()
    main_window.title(team)
    main_window.resizable(False, False)
    window_width = 1600
    window_height = 1000

    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    x_coord = (screen_width / 2) - (window_width / 2)
    y_coord = (screen_height / 2) - (window_height / 2)
    main_window.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))

    main_window.configure(bg=assets.get('color_code', '#ffffff'))
    
    # start_calendar_frame = build_calendar(main_window, 'Start Date')
    # end_calendar_frame = build_calendar(main_window, 'End Date')

    team_info_frame = team_info.build_team_info(team, team_id, team_logos[team], main_window)
    schedule_frame = schedule.build_schedule_frame(team_id, main_window)
    # injured_list_frame = injured_list.build_injured_list_frame(team_id, main_window)
    # transactions_frame = transactions.build_transactions_frame(team_id, main_window, datetime.date(2025, 2, 1), datetime.date.today())

    # Configure grid layout
    team_info_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nw')
    schedule_frame.grid(row=1, column=0, padx=10, pady=(0, 10), sticky='nw')
    # injured_list_frame.grid(row=0, column=2, padx=10, pady=10, sticky='ne')
    # transactions_frame.grid(row=2, column=2, padx=10, pady=10, sticky='se')

    # Create a frame for the subcolumns in column 2, row 1
    # calendar_frame = tk.Frame(main_window, bg='#ffffff')
    # calendar_frame.grid(row=1, column=2, padx=10, pady=10, sticky='ne')

    # start_calendar_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ne')
    # end_calendar_frame.grid(row=0, column=1, padx=10, pady=10, sticky='ne')

    main_window.grid_columnconfigure((0, 1, 2), weight=1)
    main_window.grid_rowconfigure((0, 1, 2), weight=1)

def build_calendar(main_window: Tk, title: str) -> Frame:

    frame = tk.Frame(main_window, bg='#ffffff', bd=5, relief=SOLID, width=100, height=100)

    # Display calendar title
    title_label = tk.Label(frame, text=title, font = ('Calibri', 16), bg = 'white')
    title_label.pack(pady=5)

    day = 1
    if title == 'End Date':
        day = today.day

    date_select = Calendar(frame, selectmode='day', year=today.year, month=today.month, day=day)
    date_select.pack(pady=20)

    return frame