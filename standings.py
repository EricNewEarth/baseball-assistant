import statsapi
import datetime
import logo_paths
import pandas as pd

logos = logo_paths.logos

def get_current_standings() -> pd.DataFrame:

    standings = statsapi.standings_data(season=statsapi.latest_season()['seasonId'])

    rows = []
    for division in standings.values():
        div_name = division['div_name']
        for team in division['teams']:
            rows.append({
                'div_name': div_name,
                'team_name': team['name'],
                'div_rank': team['div_rank']
            })

    standings_data = pd.DataFrame(rows)

    al_east = standings_data[standings_data['div_name'] == 'American League East']
    al_central = standings_data[standings_data['div_name'] == 'American League Central']
    al_west = standings_data[standings_data['div_name'] == 'American League West']
    nl_east = standings_data[standings_data['div_name'] == 'National League East']
    nl_central = standings_data[standings_data['div_name'] == 'National League Central']
    nl_west = standings_data[standings_data['div_name'] == 'National League West']

    standings = [al_east, al_central, al_west, nl_east, nl_central, nl_west]

    return standings

def get_standings_images() -> list[pd.DataFrame]:

    standings = get_current_standings()

    # Add the image column to each DataFrame in the list
    for div in standings:
        div['image'] = div['team_name'].map(logos)
    
    return standings