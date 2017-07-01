import pandas as pd
import yaml
import collections

def load_yaml(filename):
    ext = ".yaml"
    filename = str(filename)+ext
    f = open('./files/%s'%filename)
    dic_obj = yaml.load(f)
    f.close()
    return dic_obj

def flatten_dic(dic,result=None):
    if result is None:
        result = {}
    for key,value in dic.items():
        if isinstance(value, dict):
            value1 = {}
            for keyIn in value:
                value1["_".join([key,keyIn])]=value[keyIn]
            flatten_dic(value1, result)
        elif isinstance(value, (list, tuple)):
            for index, element in enumerate(value):
                if isinstance(element, dict):
                    value1 = {}
                    for keyIn in element:
                        value1["_".join([key,str(keyIn)])]=value[index][keyIn]
                    flatten_dic(value1, result)
        else:
            result[key]=value
    return result

def sort_dic(dic):
    sorted_result = collections.OrderedDict(sorted(dic.items()))
    return sorted_result

def runs_scored(match_code):
    # load the yaml file
    nested_dic = load_yaml(match_code)

    # flatten the nested_dic obtained by loading yaml file
    flattened_dic = flatten_dic(nested_dic)

    # sort the flattened_dic
    sorted_flattened_dic = sort_dic(flattened_dic)

    # lists to hold all the values
    innings_1st_batsman_list = []
    innings_1st_runs_scored = []
    innings_2nd_batsman_list = []
    innings_2nd_runs_scored = []
    innings_1st_team = []
    innings_2nd_team = []

    # get the list to batsman and their runs scored in both the innings
    for key,value in sorted_flattened_dic.items():
        if 'batsman' in key and 'innings_1st' in key:
            if type(value) is str:
                innings_1st_batsman_list.append(value)
            else:
                innings_1st_runs_scored.append(value)
        elif 'batsman' in key and 'innings_2nd' in key:
            if type(value) is str:
                innings_2nd_batsman_list.append(value)
            else:
                innings_2nd_runs_scored.append(value)

    # get the team names based on the batting team in each innings
    innings_1st_team.append(sorted_flattened_dic['innings_1st innings_team'])
    innings_2nd_team.append(sorted_flattened_dic['innings_2nd innings_team'])

    # create a dataframe for batting team in 1st inning
    dataframe1 = pd.DataFrame()
    dataframe1 = pd.DataFrame(innings_1st_batsman_list)
    dataframe1 = dataframe1.rename(columns={0:'batsman'})
    dataframe1['runs'] = pd.DataFrame(innings_1st_runs_scored)
    dataframe1['team'] = pd.DataFrame(innings_1st_team)
    dataframe1['team'] = dataframe1['team'].fillna('Kolkata Knight Riders')

    # create a dataframe for batting team in 2nd inning
    dataframe2 = pd.DataFrame()
    dataframe2 = pd.DataFrame(innings_2nd_batsman_list)
    dataframe2 = dataframe2.rename(columns={0:'batsman'})
    dataframe2['runs'] = pd.DataFrame(innings_2nd_runs_scored)
    dataframe2['team'] = pd.DataFrame(innings_2nd_team)
    dataframe2['team'] = dataframe2['team'].fillna('Royal Challengers Bangalore')

    # merge the two dataframes
    runs_scored_dataframe = pd.concat([dataframe1,dataframe2])

    # group by batsman and team and find the runs scored
    runs_scored_dataframe = runs_scored_dataframe.groupby(['batsman','team']).sum().reset_index().sort_values('team')

    # return the final dataframe
    return runs_scored_dataframe

def balls_faced(match_code):
    # load the yaml file
    nested_dic = load_yaml(match_code)

    # flatten the nested_dic obtained by loading yaml file
    flattened_dic = flatten_dic(nested_dic)

    # sort the flattened_dic
    sorted_flattened_dic = sort_dic(flattened_dic)

    # lists to hold all the values
    innings_1st_batsman_list = []
    innings_2nd_batsman_list = []
    innings_1st_team = []
    innings_2nd_team = []

    # get the list of strikers in both the innings
    for key,value in sorted_flattened_dic.items():
        if 'batsman' in key and 'innings_1st' in key:
            if type(value) is str:
                innings_1st_batsman_list.append(value)
        elif 'batsman' in key and 'innings_2nd' in key:
            if type(value) is str:
                innings_2nd_batsman_list.append(value)

    # get the team names based on the batting team in each innings
    innings_1st_team.append(sorted_flattened_dic['innings_1st innings_team'])
    innings_2nd_team.append(sorted_flattened_dic['innings_2nd innings_team'])

    # create dataframe for strikers in 1st inning
    dataframe1 = pd.DataFrame()
    dataframe1 = pd.DataFrame(innings_1st_batsman_list)
    dataframe1 = dataframe1.rename(columns={0:'batsman'})
    dataframe1['team'] = pd.DataFrame(innings_1st_team)
    dataframe1['team'] = dataframe1['team'].fillna('Kolkata Knight Riders')

    # create dataframe for strikers in 2nd inning
    dataframe2 = pd.DataFrame()
    dataframe2 = pd.DataFrame(innings_2nd_batsman_list)
    dataframe2 = dataframe2.rename(columns={0:'batsman'})
    dataframe2['team'] = pd.DataFrame(innings_2nd_team)
    dataframe2['team'] = dataframe2['team'].fillna('Royal Challengers Bangalore')

    # merge the two dataframes
    balls_faced_dataframe = pd.concat([dataframe1,dataframe2])

    # group by batsman to get the balls faced by each
    balls_faced = pd.DataFrame(balls_faced_dataframe.groupby(['batsman','team'])['batsman'].count())
    balls_faced = balls_faced.rename(columns={'batsman':'balls_faced'})
    balls_faced = balls_faced.reset_index()

    # return the final dataframe
    return balls_faced

def balls_bowled(match_code):
    # load the yaml file
    nested_dic = load_yaml(match_code)

    # flatten the nested_dic obtained by loading yaml file
    flattened_dic = flatten_dic(nested_dic)

    # sort the flattened_dic
    sorted_flattened_dic = sort_dic(flattened_dic)

    # lists to hold all the values
    innings_1st_bowlers_list = []
    innings_2nd_bowlers_list = []
    innings_1st_team = []
    innings_2nd_team = []

    # get the list of bowlers in both the innings
    for key,value in sorted_flattened_dic.items():
        if 'bowler' in key and 'innings_1st' in key:
            if type(value) is str:
                innings_1st_bowlers_list.append(value)
        elif 'bowler' in key and 'innings_2nd' in key:
            if type(value) is str:
                innings_2nd_bowlers_list.append(value)

    # get the team names based on the bowling team in each innings
    innings_1st_team.append(sorted_flattened_dic['innings_2nd innings_team'])
    innings_2nd_team.append(sorted_flattened_dic['innings_1st innings_team'])

    # create dataframe for bowlers in 1st inning
    dataframe1 = pd.DataFrame()
    dataframe1 = pd.DataFrame(innings_1st_bowlers_list)
    dataframe1 = dataframe1.rename(columns={0:'bowlers'})
    dataframe1['team'] = pd.DataFrame(innings_1st_team)
    dataframe1['team'] = dataframe1['team'].fillna('Royal Challengers Bangalore')

    # create dataframe for bowlers in 2nd inning
    dataframe2 = pd.DataFrame()
    dataframe2 = pd.DataFrame(innings_2nd_bowlers_list)
    dataframe2 = dataframe2.rename(columns={0:'bowlers'})
    dataframe2['team'] = pd.DataFrame(innings_2nd_team)
    dataframe2['team'] = dataframe2['team'].fillna('Kolkata Knight Riders')

    # merge the two dataframes
    balls_bowled_dataframe = pd.concat([dataframe1,dataframe2])

    # group by bowler to get the balls bowled by each
    balls_bowled = pd.DataFrame(balls_bowled_dataframe.groupby(['bowlers','team'])['bowlers'].count())
    balls_bowled = balls_bowled.rename(columns={'bowlers':'balls_bowled'})
    balls_bowled = balls_bowled.reset_index()

    # return the final dataframe
    return balls_bowled

def runs_conceded(match_code):
    # load the yaml file
    nested_dic = load_yaml(match_code)

    # flatten the nested_dic obtained by loading yaml file
    flattened_dic = flatten_dic(nested_dic)

    # sort the flattened_dic
    sorted_flattened_dic = sort_dic(flattened_dic)

    # lists to hold the values
    innings_1st_bowler_list = []
    innings_2nd_bowler_list = []
    innings_1st_runs_conceded = []
    innings_2nd_runs_conceded = []
    innings_1st_team = []
    innings_2nd_team = []

    # get the list of bowlers and runs conceded by them
    for key,value in sorted_flattened_dic.items():
        if 'bowler' in key and 'innings_1st' in key:
            innings_1st_bowler_list.append(value)
        elif 'runs_total' in key and 'innings_1st' in key:
            innings_1st_runs_conceded.append(value)
        elif 'bowler' in key and 'innings_2nd' in key:
            innings_2nd_bowler_list.append(value)
        elif 'runs_total' in key and 'innings_2nd' in key:
            innings_2nd_runs_conceded.append(value)

    # get the team names based on the bowl team in each innings
    innings_1st_team.append(sorted_flattened_dic['innings_2nd innings_team'])
    innings_2nd_team.append(sorted_flattened_dic['innings_1st innings_team'])

    # create a dataframe for bowling team in 1st inning
    dataframe1 = pd.DataFrame()
    dataframe1 = pd.DataFrame(innings_1st_bowler_list)
    dataframe1 = dataframe1.rename(columns={0:'bowler'})
    dataframe1['runs_conceded'] = pd.DataFrame(innings_1st_runs_conceded)
    dataframe1['team'] = pd.DataFrame(innings_1st_team)
    dataframe1['team'] = dataframe1['team'].fillna('Royal Challengers Bangalore')

    # create a dataframe for batting team in 2nd inning
    dataframe2 = pd.DataFrame()
    dataframe2 = pd.DataFrame(innings_2nd_bowler_list)
    dataframe2 = dataframe2.rename(columns={0:'bowler'})
    dataframe2['runs_conceded'] = pd.DataFrame(innings_2nd_runs_conceded)
    dataframe2['team'] = pd.DataFrame(innings_2nd_team)
    dataframe2['team'] = dataframe2['team'].fillna('Kolkata Knight Riders')

    # merge the two dataframes
    runs_conceded_dataframe = pd.concat([dataframe1,dataframe2])

    # group by bowler and team and find the runs conceded
    runs_conceded_dataframe = runs_conceded_dataframe.groupby(['bowler','team'])['runs_conceded'].sum().reset_index().sort_values('team')

    # return the final dataframe
    return runs_conceded_dataframe

def get_teams(match_code):
    # load the yaml file
    nested_dic = load_yaml(match_code)

    # flatten the nested_dic obtained by loading yaml file
    flattened_dic = flatten_dic(nested_dic)

    # sort the flattened_dic
    sorted_flattened_dic = sort_dic(flattened_dic)

    teams = []
    teams.append(sorted_flattened_dic['innings_1st innings_team'])
    teams.append(sorted_flattened_dic['innings_2nd innings_team'])

    # return list of teams
    return teams

def get_first_batsman(match_code):
    # load the yaml file
    nested_dic = load_yaml(match_code)

    # flatten the nested_dic obtained by loading yaml file
    flattened_dic = flatten_dic(nested_dic)

    # sort the flattened_dic
    sorted_flattened_dic = sort_dic(flattened_dic)

    innings_1st_batsman_list = []

    # list the batsmen in 1st inning
    for key,value in sorted_flattened_dic.items():
        if 'batsman' in key and 'innings_1st' in key:
            if type(value) is str:
                innings_1st_batsman_list.append(value)
    # return the first batsman
    return innings_1st_batsman_list[0]

def get_winner(match_code):
    # load the yaml file
    nested_dic = load_yaml(match_code)

    # flatten the nested_dic obtained by loading yaml file
    flattened_dic = flatten_dic(nested_dic)

    # sort the flattened_dic
    sorted_flattened_dic = sort_dic(flattened_dic)

    # return the winner
    return sorted_flattened_dic['info_outcome_winner']
