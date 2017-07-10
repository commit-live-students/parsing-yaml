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

# Question 1: Write a function that returns how many runs were scored by each batsman?

def runs_scored(match_code):
    df = generate_dataframe(match_code)
    return df.groupby(['Batsmans','Team']).agg({'Runs_Scored':np.sum})

# Question 2: Write a function that returns how many balls were faced by each batsman?

def balls_faced(match_code):
    df = generate_dataframe(match_code)
    df1 = df.groupby(['Batsmans','Team'])['Runs_Scored'].count()
    df2 = pd.DataFrame(df1)
    df3 = df2.rename(columns={'Runs_Scored':'Balls_Faced'})
    return df3

# Question 3: Write a function that returns how many balls were balled by each bowler?

def balls_bowled(match_code):
    df = generate_dataframe(match_code)
    df1 = df.groupby(['Bowler','Team'])['Balls'].count()
    df2 = pd.DataFrame(df1)
    return df2.rename(columns={'Balls':'Balls_Bowled'})

# Question 4: Write a function that returns how many runs were conceded by each bowler?

def runs_conceded(match_code):
    df = generate_dataframe(match_code)
    return df.groupby(['Bowler','Team']).agg({'Runs_Conceded':np.sum})

# Question 5: Write a function that returns name of the teams.

def get_teams(match_code):
    data = generate_data(match_code)
    return data['info']['teams']

# Question 6: Write a function that returns who batted first?

def get_first_batsman(match_code):
    data = generate_data(match_code)
    return data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']

# Question 7: Write a function that returns who won?

def get_winner(match_code):
    data = generate_data(match_code)
    return data['info']['outcome']['winner']
