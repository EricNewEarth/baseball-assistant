import logo_paths

tp_logos = logo_paths.get_tp_logos()

def return_assets(team):
    if team == 'Arizona Diamondbacks':
        return tp_logos[0] + ['https://www.cbssports.com/mlb/teams/ARI/arizona-diamondbacks/', 'https://www.mlb.com/dbacks/roster/transactions', 'https://www.mlb.com/dbacks/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/ARI/arizona-diamondbacks/injuries/', 'https://www.cbssports.com/mlb/teams/ARI/arizona-diamondbacks/schedule/', '#A71930']
    elif team == 'Atlanta Braves':
        return tp_logos[1] + ['https://www.cbssports.com/mlb/teams/ATL/atlanta-braves/', 'https://www.mlb.com/braves/roster/transactions', 'https://www.mlb.com/braves/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/ATL/atlanta-braves/injuries/', 'https://www.cbssports.com/mlb/teams/ATL/atlanta-braves/schedule/', '#13274F']
    elif team == 'Baltimore Orioles':
        return tp_logos[2] + ['https://www.cbssports.com/mlb/teams/BAL/baltimore-orioles/', 'https://www.mlb.com/orioles/roster/transactions', 'https://www.mlb.com/orioles/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/BAL/baltimore-orioles/injuries/', 'https://www.cbssports.com/mlb/teams/BAL/baltimore-orioles/schedule/', '#DF4601']
    elif team == 'Boston Red Sox':
        return tp_logos[3] + ['https://www.cbssports.com/mlb/teams/BOS/boston-red-sox/', 'https://www.mlb.com/redsox/roster/transactions', 'https://www.mlb.com/redsox/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/BOS/boston-red-sox/injuries/', 'https://www.cbssports.com/mlb/teams/BOS/boston-red-sox/schedule/', '#BD3039']
    elif team == 'Chicago Cubs':
        return tp_logos[4] + ['https://www.cbssports.com/mlb/teams/CHC/chicago-cubs/', 'https://www.mlb.com/cubs/roster/transactions', 'https://www.mlb.com/cubs/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/CHC/chicago-cubs/injuries/', 'https://www.cbssports.com/mlb/teams/CHC/chicago-cubs/schedule/', '#0E3386']
    elif team == 'Chicago White Sox':
        return tp_logos[5] + ['https://www.cbssports.com/mlb/teams/CHW/chicago-white-sox/', 'https://www.mlb.com/whitesox/roster/transactions', 'https://www.mlb.com/whitesox/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/CHW/chicago-white-sox/injuries/', 'https://www.cbssports.com/mlb/teams/CHW/chicago-white-sox/schedule/', '#27251F']
    elif team == 'Cincinnati Reds':
        return tp_logos[6] + ['https://www.cbssports.com/mlb/teams/CIN/cincinnati-reds/', 'https://www.mlb.com/reds/roster/transactions', 'https://www.mlb.com/reds/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/CIN/cincinnati-reds/injuries/', 'https://www.cbssports.com/mlb/teams/CIN/cincinnati-reds/schedule/', '#C6011F']
    elif team == 'Cleveland Guardians':
        return tp_logos[7] + ['https://www.cbssports.com/mlb/teams/CLE/cleveland-guardians/', 'https://www.mlb.com/guardians/roster/transactions/', 'https://www.mlb.com/guardians/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/CLE/cleveland-guardians/injuries/', 'https://www.cbssports.com/mlb/teams/CLE/cleveland-guardians/schedule/', '#00385D']
    elif team == 'Colorado Rockies':
        return tp_logos[8] + ['https://www.cbssports.com/mlb/teams/COL/colorado-rockies/', 'https://www.mlb.com/rockies/roster/transactions', 'https://www.mlb.com/rockies/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/COL/colorado-rockies/injuries/', 'https://www.cbssports.com/mlb/teams/COL/colorado-rockies/schedule/', '#333366']
    elif team == 'Detroit Tigers':
        return tp_logos[9] + ['https://www.cbssports.com/mlb/teams/DET/detroit-tigers/', 'https://www.mlb.com/tigers/roster/transactions', 'https://www.mlb.com/tigers/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/DET/detroit-tigers/injuries/', 'https://www.cbssports.com/mlb/teams/DET/detroit-tigers/schedule/', '#0C2340']
    elif team == 'Houston Astros':
        return tp_logos[10] + ['https://www.cbssports.com/mlb/teams/HOU/houston-astros/', 'https://www.mlb.com/astros/roster/transactions', 'https://www.mlb.com/astros/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/HOU/houston-astros/injuries/', 'https://www.cbssports.com/mlb/teams/HOU/houston-astros/schedule/', '#EB6E1F']
    elif team == 'Kansas City Royals':
        return tp_logos[11] + ['https://www.cbssports.com/mlb/teams/KC/kansas-city-royals/', 'https://www.mlb.com/royals/roster/transactions/', 'https://www.mlb.com/royals/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/KC/kansas-city-royals/injuries/', 'https://www.cbssports.com/mlb/teams/KC/kansas-city-royals/schedule/', '#004687']
    elif team == 'Los Angeles Angels':
        return tp_logos[12] + ['https://www.cbssports.com/mlb/teams/LAA/los-angeles-angels/', 'https://www.mlb.com/angels/roster/transactions', 'https://www.mlb.com/angels/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/LAA/los-angeles-angels/injuries/', 'https://www.cbssports.com/mlb/teams/LAA/los-angeles-angels/schedule/', '#BA0021']
    elif team == 'Los Angeles Dodgers':
        return tp_logos[13] + ['https://www.cbssports.com/mlb/teams/LAD/los-angeles-dodgers/', 'https://www.mlb.com/dodgers/roster/transactions', 'https://www.mlb.com/dodgers/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/LAD/los-angeles-dodgers/injuries/', 'https://www.cbssports.com/mlb/teams/LAD/los-angeles-dodgers/schedule/', '#005A9C']
    elif team == 'Miami Marlins':
        return tp_logos[14] + ['https://www.cbssports.com/mlb/teams/MIA/miami-marlins/', 'https://www.mlb.com/marlins/roster/transactions/', 'https://www.mlb.com/marlins/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/MIA/miami-marlins/injuries/', 'https://www.cbssports.com/mlb/teams/MIA/miami-marlins/schedule/', '#00A3E0']
    elif team == 'Milwaukee Brewers':
        return tp_logos[15] + ['https://www.cbssports.com/mlb/teams/MIL/milwaukee-brewers/', 'https://www.mlb.com/brewers/roster/transactions', 'https://www.mlb.com/brewers/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/MIL/milwaukee-brewers/injuries/', 'https://www.cbssports.com/mlb/teams/MIL/milwaukee-brewers/schedule/', '#12284b']
    elif team == 'Minnesota Twins':
        return tp_logos[16] + ['https://www.cbssports.com/mlb/teams/MIN/minnesota-twins/', 'https://www.mlb.com/twins/roster/transactions', 'https://www.mlb.com/twins/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/MIN/minnesota-twins/injuries/', 'https://www.cbssports.com/mlb/teams/MIN/minnesota-twins/schedule/', '#002B5C']
    elif team == 'New York Mets':
        return tp_logos[17] + ['https://www.cbssports.com/mlb/teams/NYM/new-york-mets/', 'https://www.mlb.com/mets/roster/transactions', 'https://www.mlb.com/mets/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/NYM/new-york-mets/injuries/', 'https://www.cbssports.com/mlb/teams/NYM/new-york-mets/schedule/', '#002D72']  
    elif team == 'New York Yankees':
        return tp_logos[18] + ['https://www.cbssports.com/mlb/teams/NYY/new-york-yankees/', 'https://www.mlb.com/yankees/roster/transactions', 'https://www.mlb.com/yankees/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/NYY/new-york-yankees/injuries/', 'https://www.cbssports.com/mlb/teams/NYY/new-york-yankees/schedule/', '#0C2340']
    elif team == 'Oakland Athletics':
        return tp_logos[19] + ['https://www.cbssports.com/mlb/teams/OAK/oakland-athletics/', 'https://www.mlb.com/athletics/roster/transactions', 'https://www.mlb.com/athletics/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/OAK/oakland-athletics/injuries/', 'https://www.cbssports.com/mlb/teams/OAK/oakland-athletics/schedule/', '#003831']
    elif team == 'Philadelphia Phillies':
        return tp_logos[20] + ['https://www.cbssports.com/mlb/teams/PHI/philadelphia-phillies/', 'https://www.mlb.com/phillies/roster/transactions', 'https://www.mlb.com/phillies/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/PHI/philadelphia-phillies/injuries/', 'https://www.cbssports.com/mlb/teams/PHI/philadelphia-phillies/schedule/', '#E81828']
    elif team == 'Pittsburgh Pirates':
        return tp_logos[21] + ['https://www.cbssports.com/mlb/teams/PIT/pittsburgh-pirates/', 'https://www.mlb.com/pirates/roster/transactions', 'https://www.mlb.com/pirates/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/PIT/pittsburgh-pirates/injuries/', 'https://www.cbssports.com/mlb/teams/PIT/pittsburgh-pirates/schedule/', '#FDB827']
    elif team == 'San Diego Padres':
        return tp_logos[22] + ['https://www.cbssports.com/mlb/teams/SD/san-diego-padres/', 'https://www.mlb.com/padres/roster/transactions', 'https://www.mlb.com/padres/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/SD/san-diego-padres/injuries/', 'https://www.cbssports.com/mlb/teams/SD/san-diego-padres/schedule/', '#2F241D']
    elif team == 'San Francisco Giants':
        return tp_logos[23] + ['https://www.cbssports.com/mlb/teams/SF/san-francisco-giants/', 'https://www.mlb.com/giants/roster/transactions', 'https://www.mlb.com/giants/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/SF/san-francisco-giants/injuries/', 'https://www.cbssports.com/mlb/teams/SF/san-francisco-giants/schedule/', '#FD5A1E']
    elif team == 'Seattle Mariners':
        return tp_logos[24] + ['https://www.cbssports.com/mlb/teams/SEA/seattle-mariners/', 'https://www.mlb.com/mariners/roster/transactions', 'https://www.mlb.com/mariners/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/SEA/seattle-mariners/injuries/', 'https://www.cbssports.com/mlb/teams/SEA/seattle-mariners/schedule/', '#005C5C']
    elif team == 'St. Louis Cardinals':
        return tp_logos[25] + ['https://www.cbssports.com/mlb/teams/STL/st-louis-cardinals/', 'https://www.mlb.com/cardinals/roster/transactions', 'https://www.mlb.com/cardinals/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/STL/st-louis-cardinals/injuries/', 'https://www.cbssports.com/mlb/teams/STL/st-louis-cardinals/schedule/', '#C41E3A']
    elif team == 'Tampa Bay Rays':
        return tp_logos[26] + ['https://www.cbssports.com/mlb/teams/TB/tampa-bay-rays/', 'https://www.mlb.com/rays/roster/transactions', 'https://www.mlb.com/rays/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/TB/tampa-bay-rays/injuries/', 'https://www.cbssports.com/mlb/teams/TB/tampa-bay-rays/schedule/', '#8FBCE6']
    elif team == 'Texas Rangers':
        return tp_logos[27] + ['https://www.cbssports.com/mlb/teams/TEX/texas-rangers/', 'https://www.mlb.com/rangers/roster/transactions', 'https://www.mlb.com/rangers/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/TEX/texas-rangers/injuries/', 'https://www.cbssports.com/mlb/teams/TEX/texas-rangers/schedule/', '#003278']
    elif team == 'Toronto Blue Jays':
        return tp_logos[28] + ['https://www.cbssports.com/mlb/teams/TOR/toronto-blue-jays/', 'https://www.mlb.com/bluejays/roster/transactions', 'https://www.mlb.com/bluejays/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/TOR/toronto-blue-jays/injuries/', 'https://www.cbssports.com/mlb/teams/TOR/toronto-blue-jays/schedule/', '#134A8E']
    elif team == 'Washington Nationals':
        return tp_logos[29] + ['https://www.cbssports.com/mlb/teams/WAS/washington-nationals/', 'https://www.mlb.com/nationals/roster/transactions', 'https://www.mlb.com/nationals/roster/depth-chart', 'https://www.cbssports.com/mlb/teams/WAS/washington-nationals/injuries/', 'https://www.cbssports.com/mlb/teams/WAS/washington-nationals/schedule/', '#AB0003']