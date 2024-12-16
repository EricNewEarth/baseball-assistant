import requests
import logo_paths
from bs4 import BeautifulSoup

def get_current_standings():
    al_east = []
    al_central = []
    al_west = []
    nl_east = []
    nl_central = []
    nl_west = []

    # Send a GET request to the standings page
    standings_url = 'https://www.baseball-reference.com/leagues/MLB-standings.shtml'
    response = requests.get(standings_url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Grab division table elements
    divisions = soup.find_all('div', id = 'all_standings')

    # Grab AL Division element
    al_divisions = divisions[0]

    # Grab AL East title element for each team
    al_east_standings = al_divisions.find('table', id = 'standings_E')
    al_east_teams = al_east_standings.find_all('a')
    for team in al_east_teams:
        al_east.append(team['title'])
    
    # Grab AL Central title element for each team
    al_central_standings = al_divisions.find('table', id = 'standings_C')
    al_central_teams = al_central_standings.find_all('a')
    for team in al_central_teams:
        al_central.append(team['title'])

    # Grab AL West title element for each team
    al_west_standings = al_divisions.find('table', id = 'standings_W')
    al_west_teams = al_west_standings.find_all('a')
    for team in al_west_teams:
        al_west.append(team['title'])
    
    # Grab NL Division element
    nl_divisions = divisions[1]

    # Grab NL East title element for each team
    nl_east_standings = nl_divisions.find('table', id = 'standings_E')
    nl_east_teams = nl_east_standings.find_all('a')
    for team in nl_east_teams:
        nl_east.append(team['title'])
    
    # Grab NL Central title element for each team
    nl_central_standings = nl_divisions.find('table', id = 'standings_C')
    nl_central_teams = nl_central_standings.find_all('a')
    for team in nl_central_teams:
        nl_central.append(team['title'])

    # Grab NL West title element for each team
    nl_west_standings = nl_divisions.find('table', id = 'standings_W')
    nl_west_teams = nl_west_standings.find_all('a')
    for team in nl_west_teams:
        nl_west.append(team['title'])

    standings = [al_east, al_central, al_west, nl_east, nl_central, nl_west]
    return standings

def get_image_order():
    # Grab current MLB standings order
    current_standings = get_current_standings()
    team_logos = logo_paths.get_logos()
    order = standings_order(current_standings)
    
    # Construct team image grid order
    image_order = []
    for team in order:
        for logo in team_logos:
            if logo[0] == team:
                image_order.append(logo[1])
                break

    return image_order

def standings_order(current_standings):
    order = []
    al_east = current_standings[0]
    al_central = current_standings[1]
    al_west = current_standings[2]
    nl_east = current_standings[3]
    nl_central = current_standings[4]
    nl_west = current_standings[5]

    # Append teams from each division by current place
    for i in range(0, 5):
        order.append(al_east[i]) 
        order.append(al_central[i])
        order.append(al_west[i])
        order.append(nl_east[i])
        order.append(nl_central[i])
        order.append(nl_west[i])

    return order