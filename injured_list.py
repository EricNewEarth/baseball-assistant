import statsapi
import tkinter as tk
from tkinter import *

def build_injured_list_frame(team_id, main_window):

    frame = tk.Frame(main_window, bg='#ffffff', bd=5, relief=SOLID, width = 100, height = 600)

    # Display schedule title
    title_label = tk.Label(frame, text = 'Injured List', font = ('Calibri', 16), bg = 'white')
    title_label.pack(pady=5)

    roster = statsapi.get('team_roster', {'teamId': team_id})['roster']
    for player in roster:
        print(player)
    injured_list = []

    # for player in roster:
    #     player_name = player[9:]
    #     player_results = statsapi.lookup_player(player_name)
    #     player_info = []
    #     for p in player_results:
    #         if p.get('current_team', {}).get('id', 0) == team_id:
    #             player_info = p
    #             break

    #     print(player_info)

    return frame