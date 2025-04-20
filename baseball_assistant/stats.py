import pytz
import statsapi
import datetime
import pandas as pd

def get_schedule(team_id):

    start_date = (datetime.date.today() - datetime.timedelta(days=2)).strftime('%Y-%m-%d')
    end_date = (datetime.date.today() + datetime.timedelta(days=7)).strftime('%Y-%m-%d')

    schedule = statsapi.schedule(team=team_id, start_date=start_date, end_date=end_date)