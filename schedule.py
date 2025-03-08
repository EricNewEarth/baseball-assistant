import pytz
import statsapi
import datetime
import team_assets
import tkinter as tk
from tkinter import *

def build_schedule_frame(team_id, main_window):
    
    frame = tk.Frame(main_window, bg='#ffffff', bd=5, relief=SOLID, width = 100, height = 600)

    # Display schedule title
    title_label = tk.Label(frame, text = 'Schedule Glance', font = ('Calibri', 16), bg = 'white')
    title_label.pack(pady=5)

    start_date = (datetime.date.today() - datetime.timedelta(days=2)).strftime('%Y-%m-%d')
    end_date = (datetime.date.today() + datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    
    # Get team schedule from id
    schedule = statsapi.schedule(team=team_id, start_date=start_date, end_date=end_date)

    for game in schedule[:8]:

        status = game.get('status', '')
        game_date = game.get('game_date', '')
        game_date = datetime.datetime.strptime(game_date, '%Y-%m-%d').strftime('%m/%d/%Y')
        time_utc = game.get('game_datetime', '')
        
        # Convert time to 12-hour format in local timezone
        if time_utc:
            utc_time = datetime.datetime.strptime(time_utc, '%Y-%m-%dT%H:%M:%SZ')
            local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('America/New_York'))
            time = local_time.strftime('%I:%M %p')
        else:
            time = 'TBD'

        if status == 'Delayed':
            time = 'Delayed'
        
        try:
            away_team = team_assets.return_assets(game.get('away_name', '')).get('abbr', '')
            home_team = team_assets.return_assets(game.get('home_name', '')).get('abbr', '')
        except KeyError:
            away_team = game.get('away_name', '')
            home_team = game.get('home_name', '')
            
        away_pitcher = game.get('away_probable_pitcher', 'TBD')
        home_pitcher = game.get('home_probable_pitcher', 'TBD')
        away_pitcher_name = away_pitcher.split(' ', 1)[1] if ' ' in away_pitcher else 'TBD'
        home_pitcher_name = home_pitcher.split(' ', 1)[1] if ' ' in home_pitcher else 'TBD'
        matchup = f'{away_pitcher_name} vs {home_pitcher_name}'

        if status == 'Scheduled' or status == 'Pre-Game' or status == 'Warmup':
            game_info = f'{game_date} - {time}\n{away_team} @ {home_team}\n{matchup:^20}'
        elif status == 'In Progress' or status == 'Delayed':
            inning = f'{game.get("inning_state", "")} {game.get("current_inning", "")}'
            score = f'{away_team}: {game.get("away_score", "")} @ {home_team}: {game.get("home_score", "")}'
            venue = game.get('venue_name', '')
            game_info = f'{game_date} - {inning}\n{score:^20}\n{venue:^20}'
        else:
            score = f'{away_team}: {game.get("away_score", "")} @ {home_team}: {game.get("home_score", "")}'
            winning_pitcher = game.get('winning_pitcher', '')
            losing_pitcher = game.get('losing_pitcher', '')
            save_pitcher = game.get('save_pitcher', '')
            winning_pitcher_name = winning_pitcher.split(' ', 1)[1] if winning_pitcher and ' ' in winning_pitcher else ''
            losing_pitcher_name = losing_pitcher.split(' ', 1)[1] if losing_pitcher and ' ' in losing_pitcher else ''
            save_pitcher_name = save_pitcher.split(' ', 1)[1] if save_pitcher and ' ' in save_pitcher else ''
            summary = f'W: {winning_pitcher_name}, L: {losing_pitcher_name}'
            if save_pitcher_name:
                summary += f', SV: {save_pitcher_name}'
            game_info = f'{game_date} - {status}\n{score:^20}\n{summary:^20}'

        game_label = tk.Label(frame, text=game_info, font=('Calibri', 12), bg='white', justify='center', width=44)
        game_label.pack(anchor='w', pady=5)

    return frame