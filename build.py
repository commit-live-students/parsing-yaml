import pandas as pd
import numpy as np
import yaml

def generate_data(match_code):
    match_code = 'files/'+str(match_code)+'.yaml'
    with open(match_code, 'r') as stream:
        data = yaml.load(stream)
    return data

def generate_dataframe(match_code):
    data = generate_data(match_code)
    all_list = []
    teams = []
    summation = []
    for elem in data['innings']:
        for innings in elem:
            for deliveries, values in elem[innings].items():
                if deliveries == 'team':
                    teams.append(values)
                else:
                    for overs in values:
                        if type(overs) == str:
                            continue
                        else:
                            for key, value in overs.items():
                                summation.append(key)
                                new_dict = {
                                            'batsman' : value['batsman'],
                                            'bowler': value['bowler'],
                                            'non_striker': value['non_striker'],
                                            'batsman_runs': value['runs']['batsman'],
                                            'extra_runs': value['runs']['extras'],
                                            'total_runs': value['runs']['total'],
                                            'balls': key,
                                            'teams' : elem[innings]['team']
                                            }
                                all_list.append(new_dict)
    #     all_list
#     print teams[0]
    df = pd.DataFrame(all_list)
    return df

def runs_scored(match_code):
    df = generate_dataframe(match_code)
    group = df.groupby(['batsman', 'teams'])
    df_sum = group.agg({'batsman_runs': np.sum})
    df_sum = pd.DataFrame(df_sum)
    df_sum = df_sum.rename(columns=({'batsman_runs': 'Runs_Scored'}))
    return df_sum

def balls_faced(match_code):
    df = generate_dataframe(match_code)
    group = df.groupby(['batsman', 'teams'])['batsman_runs'].count()
    df1 = pd.DataFrame(group)
    # df_ball
    df1 = df1.rename(columns={'batsman_runs': 'balls_faced'})
    return df1


def balls_bowled(match_code):
    df = generate_dataframe(match_code)
    group = df.groupby(['bowler', 'teams'])['balls'].count()
    df1 = pd.DataFrame(group)
    # df_ball
    df1 = df1.rename(columns={'balls': 'balls_bowled'})
    return df1


def runs_conceded(match_code):
    df = generate_dataframe(match_code)
    group = df.groupby(['bowler', 'teams'])
    df_sum = group.agg({'batsman_runs': np.sum})
    df_sum = pd.DataFrame(df_sum)
    df_sum = df_sum.rename(columns={'batsman_runs': 'Runs_Conceded'})
    return df_sum


def get_teams(match_code):
    data = generate_data(match_code)
    teams = data['info']['teams']
    return teams

def get_first_batsman(match_code):
    # df = generate_dataframe(match_code)
    data = generate_data(match_code)
    return data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']

def get_winner(match_code):
    data = generate_data(match_code)
    return data['info']['outcome']['winner']
