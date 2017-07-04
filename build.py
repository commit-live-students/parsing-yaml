import numpy as np
import pandas as pd
import yaml

def generate_data(match_code):
    filename = "files/"+str(match_code)+".yaml"
    with open(filename) as f:
        data = yaml.load(f)
    return data

def generate_dataframe(match_code):
    data = generate_data(match_code)
    info = data['innings']
    all_data = []
    for extracted_ip in info:
        for innings_value in extracted_ip.keys():
            info_list = extracted_ip[innings_value]['deliveries']
            for each_ball in info_list:
                for ball, innings_list in each_ball.items():
                    new_dict = {'Batsmans':innings_list['batsman'],
                                'Team':extracted_ip[innings_value]['team'],
                                'Bowler':innings_list['bowler'],
                                'Non_striker':innings_list['non_striker'],
                                'Runs_Scored':innings_list['runs']['batsman'],
                                'Runs_Conceded':innings_list['runs']['total'],
                                'Te':innings_list['runs']['extras'],
                                'Balls':ball}
                    all_data.append(new_dict)
    ref_innings = pd.DataFrame(all_data)
    return ref_innings

def runs_scored(match_code):
    t = generate_dataframe(match_code)
    return t.groupby(['Batsmans','Team']).agg({'Runs_Scored':np.sum})

def balls_faced(match_code):
    t = generate_dataframe(match_code)
    t = t.groupby(['Batsmans','Team'])['Runs_Scored'].count()
    u = pd.DataFrame(t)
    u = u.rename(columns={'Runs_Scored':'Balls_Faced'})
    return u

def balls_bowled(match_code):
    t = generate_dataframe(match_code)
    t = t.groupby(['Bowler','Team'])['Balls'].count()
    u = pd.DataFrame(t)
    u = u.rename(columns={'Balls':'Balls_Bowled'})
    return u

def runs_conceded(match_code):
    t = generate_dataframe(match_code)
    return t.groupby(['Bowler','Team']).agg({'Runs_Conceded':np.sum})

def get_teams(match_code):
    data = generate_data(match_code)
    return data['info']['teams']

def get_first_batsman(match_code):
    data = generate_data(match_code)
    return data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']

def get_winner(match_code):
    data = generate_data(match_code)
    return data['info']['outcome']['winner']

print balls_faced(335982)
