import yaml
import pandas as pd
from collections import OrderedDict

def flatten_dict (aDict, otherDict):
    flatdict = {}
    for key, value in aDict.items():
        if isinstance (value, dict):
            for key2, value2 in value.items():
                flatdict[key + "_" + key2] = value2;
        else:
            flatdict[key] = value
    flatdict.update(otherDict)
    return flatdict

def get_yaml_content (match_code):
    coontent = ""
    with open("files/"+ str(match_code) + ".yaml", 'r') as stream:
        try:
            content = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return content

def get_innings (match_code):
    content = get_yaml_content (match_code)
    innings = []
    innings = content['innings']
    return innings

def get_innings_data (match_code):
    i = 0
    deliveries = []
    for inning in get_innings (match_code):
        team = inning.values()[0]['team']
        for bteam in get_teams (match_code):
            if bteam != team:
                break
        for elem in inning.values()[0]['deliveries']:
            deliveries.append(flatten_dict(elem.values()[0],{'Team':team, 'BTeam': bteam}))
    df = pd.DataFrame(deliveries)
    df.rename(columns = {'batsman':'Batsman','bowler': 'Bowler'}, inplace = True)

    return df

def runs_scored(match_code):
    runs = get_innings_data(match_code).groupby(['Batsman','Team']).agg({'runs_batsman':['sum']})
    runs.columns = ["_".join(x) for x in runs.columns.ravel()]
    runs.rename(columns = {'runs_batsman_sum':'Runs_Scored'}, inplace = True)
    return runs

def balls_faced(match_code):
    balls = get_innings_data(match_code).groupby(['Batsman','Team']).size().reset_index(name='Balls_Faced')
    return balls


def balls_bowled(match_code):
    balls = get_innings_data(match_code).groupby(['Bowler','BTeam']).size().reset_index(name='Balls_Bowled')
    return balls


def runs_conceded(match_code):
    runs = get_innings_data(match_code).groupby(['Bowler','BTeam']).agg({'runs_total':['sum']})
    runs.columns = ["_".join(x) for x in runs.columns.ravel()]
    runs.rename(columns = {'runs_total_sum':'Runs_Conceded'}, inplace = True)
    return runs


def get_teams(match_code):
    return [inning.values()[0]['team'] for inning in get_innings (match_code) ]


def get_first_batsman(match_code):
    return get_innings (match_code)[0]['1st innings']['deliveries'][0][0.1]['batsman']


def get_winner(match_code):
    return get_yaml_content (match_code)['info']['outcome']['winner']

if __name__ == "__main__":
    print runs_scored (335982)
    print balls_faced (335982)
    print balls_bowled(335982)
    print runs_conceded (335982)
    print
    print "The Teams Played: " + str(get_teams (335982))
    print "The First Batman: " + get_first_batsman (335982)
    print "The winner: " + get_winner(335982)
