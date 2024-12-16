# Imports
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import logo_paths
import standings
import team_assets

team_logos = logo_paths.get_logos()

def build_team_page(team_index):
    current_standings = standings.get_current_standings()
    current_standings = standings.standings_order(current_standings)
    team = current_standings[team_index]

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

    # Team assets are as follows: Name, Logo, Info Page, Transactions, Depth Chart, Injuries, Schedule, Color Code
    assets = team_assets.return_assets(team)
    team_name, team_logo, team_info_page, team_transactions, team_depth_chart, team_injuries, team_schedule, team_color = assets

    main_window.configure(bg = team_color)
    
    team_info_frame = build_team_info(team_name, team_logo, team_info_page, main_window)
    team_schedule_frame = build_schedule_glance(team_schedule, main_window)
    transaction_feed_frame = build_transaction_feed(team_transactions, main_window)
    depth_chart_frame = build_depth_chart(team_depth_chart, main_window)
    injured_list_frame = build_injured_list(team_injuries, main_window)

    team_info_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'nw')
    team_schedule_frame.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = 'ne')
    transaction_feed_frame.grid(row = 1, column = 2, padx = 10, pady = 10, sticky = 'se')
    depth_chart_frame.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = 'nsew')
    injured_list_frame.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = 'sw')

    main_window.grid_columnconfigure((0, 2), weight = 1)
    main_window.grid_rowconfigure(0, weight = 1)

def build_team_info(team_name, team_logo, team_info_page, main_window):
    # Build team info frame
    frame = tk.Frame(main_window, bg="#ffffff", bd=5, relief=SOLID, width = 100, height = 300)

    # Display team name
    name_label = tk.Label(frame, text = team_name, font = ('Calibri', 16), bg = 'white')
    name_label.pack(pady=5)

    # Display team logo
    logo_image = Image.open(team_logo)
    logo_image = logo_image.resize((250, 250))
    photo_image = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(frame, image = photo_image)
    logo_label.image = photo_image
    logo_label.pack(padx=20)

    # Grab current team record and division place
    response = requests.get(team_info_page)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find header element with data
        info = soup.find('aside', class_ = 'PageTitle-description')

        if info:
            # Extract text from the aside element
            info_text = info.get_text(strip=True)
            
            # Split the text based on the '•' character
            info_parts = info_text.split('•')

            record = info_parts[0].split(' ')
            record = record[0]
            league = info_parts[1].split(' ')
            league = league[1]
            division_place = info_parts[2].split(' ')
            place = division_place[1]
            division = division_place[2]

            info_text = f'{record}, {place} in the {league} {division}'
            info_label = tk.Label(frame, text = info_text, font = ('Calibri', 14), bg = 'white')
            info_label.pack(pady=5)
        else:
            info = 'Element was not found.'
    else:
        'Failed to fetch info page.'

    return frame

def build_transaction_feed(transactions_page, main_window):
    # Build transaction frame
    frame = tk.Frame(main_window, bg="#ffffff", bd=5, relief=SOLID, width = 100, height = 400)

    # Display transaction label
    transaction_label = tk.Label(frame, text = 'Transactions', font = ('Calibri', 16), bg = 'white')
    transaction_label.pack(pady=5)

    # Build scroll bar
    scrollbar = Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Get current year and month for transaction pages
    current_date = datetime.now()
    year = current_date.year
    month = current_date.month
    month_str = str(month).zfill(2)
    
    month_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'][::-1]
    start_index = month_list.index(month_str)
    loop_count = 0

    # Loop through the past 12 months and construct url
    transaction_pages = []
    while loop_count < 12:
        index = (start_index + loop_count) % len(month_list)
        if index == 0:
            year -= 1
        
        url = f'{transactions_page}/{year}/{month_list[index]}'
        transaction_pages.append(url)
        loop_count += 1

    transaction_pages = transaction_pages[::-1]
    
    # Grab transactions from each transaction page
    transactions = []
    for page in transaction_pages:
        response = requests.get(page)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            table = soup.find('table', class_ = 'roster__table')
            if table:
                rows = table.find_all('tr')
                rows = rows[::-1]

                for row in rows:
                    # Find the date and transaction elements
                    date_elem = row.find('td', class_ = 'date')
                    transaction_elem = row.find('td', class_ = 'description')
                    
                    # Check if both elements are found
                    if date_elem and transaction_elem:
                        # Extract text from the elements
                        date = date_elem.get_text(strip = True)
                        transaction = transaction_elem.get_text()
                        transaction = transaction.strip()

                        if [date, transaction] not in transactions:
                            transactions.append([date, transaction])
        else:
            print('Failed to fetch transactions page.')

    # Build text element to hold transactions
    font = ('Calibri', 12)

    text_widget = tk.Text(frame, wrap = tk.WORD, yscrollcommand = scrollbar.set, font = font, width = 65)
    text_widget.pack(expand = True, fill = tk.BOTH)

    transactions = transactions[::-1]
    for index, item in enumerate(transactions):
        text_widget.insert(tk.END, f'{item[0]}\t{item[1]}')
        if index < len(transactions) - 1:  # Add a new line if it's not the last item
            text_widget.insert(tk.END, '\n')

    scrollbar.config(command = text_widget.yview)

    return frame

def build_schedule_glance(schedule_page, main_window):
    # Build schedule frame
    frame = tk.Frame(main_window, bg="#ffffff", bd=5, relief=SOLID, width = 50, height = 300)

    # Display schedule label
    schedule_label = tk.Label(frame, text = 'Schedule Glance', font = ('Calibri', 16), bg = 'white')
    schedule_label.pack(pady=5)

    # Get schedule info from page
    response = requests.get(schedule_page)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        tables = soup.find_all('table', class_ = 'TableBase-table')
        prev_table = tables[0].find('tbody')
        prev_schedule = prev_table.find_all('tr', class_ = 'TableBase-bodyTr')
        next_table = tables[1].find('tbody')
        next_schedule = next_table.find_all('tr', class_ = 'TableBase-bodyTr')

        prev_three_games = []
        for index in range(1, 4):
            row = prev_schedule[len(prev_schedule) - index]
            
            date = row.find('span', class_ = 'CellGameDate').get_text(strip = True)

            home_away = row.find('span', class_ = 'CellLogoNameLockup-opposingPrefix').get_text(strip = True)
            team = row.find('span', class_ = 'TeamName').get_text(strip = True)
            opponent = f'{home_away} {team}'
            
            result = row.find('div', class_ = 'CellGame').get_text(strip = True)
            result = f'{result[0]} {result[1:]}'
            
            prev_three_games.append([date, opponent, result])

        prev_three_games = prev_three_games[::-1]
        
        next_three_games = []
        for index in range(0, 3):
            row = next_schedule[index]

            date = row.find('span', class_ = 'CellGameDate').get_text(strip = True)

            home_away = row.find('span', class_ = 'CellLogoNameLockup-opposingPrefix').get_text(strip = True)
            team = row.find('span', class_ = 'TeamName').get_text(strip = True)
            opponent = f'{home_away} {team}'

            time = row.find('div', class_ = 'CellGame').get_text(strip = True)
            time = time.split('m')
            time = f'{time[0]}m'

            next_three_games.append([date, opponent, time])

        # Add previous three games to frame with cols date, opponent, result
        prev_schedule_tree = ttk.Treeview(frame, columns = ('Date', 'Opponent', 'Result'), show = 'headings')
        prev_schedule_tree.heading('Date', text = 'Date')
        prev_schedule_tree.heading('Opponent', text = 'Opponent')
        prev_schedule_tree.heading('Result', text = 'Result')

        for game in prev_three_games:
            prev_schedule_tree.insert('', 'end', values = game)

        prev_schedule_tree.pack(fill = tk.Y)

        # Add next three games to frame with cols date, opponent, time
        next_schedule_tree = ttk.Treeview(frame, columns = ('Date', 'Opponent', 'Time'), show = 'headings')
        next_schedule_tree.heading('Date', text = 'Date')
        next_schedule_tree.heading('Opponent', text = 'Opponent')
        next_schedule_tree.heading('Time', text = 'Time')

        for game in next_three_games:
            next_schedule_tree.insert('', 'end', values = game)

        next_schedule_tree.pack(fill = tk.Y)

    else:
        print('Failed to fetch schedule page.')

    return frame

def build_depth_chart(depth_chart_page, main_window):
    frame = tk.Frame(main_window, bg="#ffffff", bd=5, relief=SOLID, width = 100, height = 300)
    
    # Display depth chart label
    depth_chart_label = tk.Label(frame, text = 'Depth Chart', font = ('Calibri', 16), bg = 'white')
    depth_chart_label.pack(pady=5)
    return frame

def build_injured_list(injured_list_page, main_window):
    frame = tk.Frame(main_window, bg="#ffffff", bd=5, relief=SOLID, width = 100, height = 300)

    # Display injured list label
    injured_list_label = tk.Label(frame, text = 'Injured List', font = ('Calibri', 16), bg = 'white')
    injured_list_label.pack(pady=5)
    return frame