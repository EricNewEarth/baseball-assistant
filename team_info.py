import statsapi
import standings
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def build_team_info(team_name, team_id, team_logo, main_window):

    # Build team info frame
    frame = tk.Frame(main_window, bg='#ffffff', bd=5, relief=SOLID, width = 100, height = 300)

    standings_record = statsapi.standings_data(season=statsapi.latest_season()['seasonId'])

    for division in standings_record.values():
        for team in division['teams']:
            if team['team_id'] == team_id:
                wins = team['w']
                losses = team['l']
                break

    name_label = f'{team_name} ({wins}-{losses})'

    # Display team name
    name_label = tk.Label(frame, text = name_label, font = ('Calibri', 15), width=35, bg = 'white')
    name_label.pack(pady=5)

    # Display team logo
    logo_image = Image.open(team_logo)
    logo_image = logo_image.resize((250, 250))
    photo_image = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(frame, image = photo_image)
    logo_label.image = photo_image
    logo_label.pack()

    # Grab current team record and division place
    current_standings = standings.get_current_standings()

    team_info = None
    for division in current_standings:
        team_info = division[division['team_name'] == team_name]
        if not team_info.empty:
            team_info = team_info.iloc[0]
            break

    if team_info is not None:
        div_rank = int(team_info['div_rank'])
        div_name = team_info['div_name']

        ordinal_suffix = {1: 'st', 2: 'nd', 3: 'rd'}
        rank_suffix = ordinal_suffix.get(div_rank, 'th')  # Default to 'th'
        rank_text = f'{div_rank}{rank_suffix}'

        league = 'AL' if 'American' in div_name else 'NL'
        division = div_name.split()[-1]

        standings_text = f'{rank_text} in the {league} {division}'
    else:
        standings_text = 'Standings not available'

    # Display team standing
    standings_label = tk.Label(frame, text = standings_text, width=35, font = ('Calibri', 15), bg = 'white')
    standings_label.pack(pady=5)

    return frame