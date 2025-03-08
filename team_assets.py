import logo_paths

logos = logo_paths.logos

def return_assets(team):
    assets = {'logo': logos[team]}
    if team == 'Arizona Diamondbacks':
        assets.update({'color_code': '#A71930', 'abbr': 'ARI'})
    elif team == 'Athletics':
        assets.update({'color_code': '#003831', 'abbr': 'ATH'})
    elif team == 'Atlanta Braves':
        assets.update({'color_code': '#13274F', 'abbr': 'ATL'})
    elif team == 'Baltimore Orioles':
        assets.update({'color_code': '#DF4601', 'abbr': 'BAL'})
    elif team == 'Boston Red Sox':
        assets.update({'color_code': '#BD3039', 'abbr': 'BOS'})
    elif team == 'Chicago Cubs':
        assets.update({'color_code': '#0E3386', 'abbr': 'CHC'})
    elif team == 'Chicago White Sox':
        assets.update({'color_code': '#27251F', 'abbr': 'CWS'})
    elif team == 'Cincinnati Reds':
        assets.update({'color_code': '#C6011F', 'abbr': 'CIN'})
    elif team == 'Cleveland Guardians':
        assets.update({'color_code': '#00385D', 'abbr': 'CLE'})
    elif team == 'Colorado Rockies':
        assets.update({'color_code': '#333366', 'abbr': 'COL'})
    elif team == 'Detroit Tigers':
        assets.update({'color_code': '#0C2340', 'abbr': 'DET'})
    elif team == 'Houston Astros':
        assets.update({'color_code': '#EB6E1F', 'abbr': 'HOU'})
    elif team == 'Kansas City Royals':
        assets.update({'color_code': '#004687', 'abbr': 'KC'})
    elif team == 'Los Angeles Angels':
        assets.update({'color_code': '#BA0021', 'abbr': 'LAA'})
    elif team == 'Los Angeles Dodgers':
        assets.update({'color_code': '#005A9C', 'abbr': 'LAD'})
    elif team == 'Miami Marlins':
        assets.update({'color_code': '#00A3E0', 'abbr': 'MIA'})
    elif team == 'Milwaukee Brewers':
        assets.update({'color_code': '#12284b', 'abbr': 'MIL'})
    elif team == 'Minnesota Twins':
        assets.update({'color_code': '#002B5C', 'abbr': 'MIN'})
    elif team == 'New York Mets':
        assets.update({'color_code': '#002D72', 'abbr': 'NYM'})  
    elif team == 'New York Yankees':
        assets.update({'color_code': '#0C2340', 'abbr': 'NYY'})
    elif team == 'Philadelphia Phillies':
        assets.update({'color_code': '#E81828', 'abbr': 'PHI'})
    elif team == 'Pittsburgh Pirates':
        assets.update({'color_code': '#FDB827', 'abbr': 'PIT'})
    elif team == 'San Diego Padres':
        assets.update({'color_code': '#2F241D', 'abbr': 'SD'})
    elif team == 'San Francisco Giants':
        assets.update({'color_code': '#FD5A1E', 'abbr': 'SF'})
    elif team == 'Seattle Mariners':
        assets.update({'color_code': '#005C5C', 'abbr': 'SEA'})
    elif team == 'St. Louis Cardinals':
        assets.update({'color_code': '#C41E3A', 'abbr': 'STL'})
    elif team == 'Tampa Bay Rays':
        assets.update({'color_code': '#8FBCE6', 'abbr': 'TB'})
    elif team == 'Texas Rangers':
        assets.update({'color_code': '#003278', 'abbr': 'TEX'})
    elif team == 'Toronto Blue Jays':
        assets.update({'color_code': '#134A8E', 'abbr': 'TOR'})
    elif team == 'Washington Nationals':
        assets.update({'color_code': '#AB0003', 'abbr': 'WSH'})

    return assets