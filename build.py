import yaml
import pandas as pd
def yaml_df_conversionn(match_code):

    with open('./files/'+str(match_code)+'.yaml','r') as line:
        yaml_content = yaml.load(line)

    return yaml_content

                #print batsman_score
                #break

def runs_scored(match_code):
    yaml_content = yaml_df_conversionn(match_code)
    cricket_df = pd.DataFrame()

    for innings in yaml_content['innings']:
        for i in innings:
            for deliveries in innings[i]['deliveries']:
                overs = list(deliveries)[0]
                over_stat = deliveries[list(deliveries)[0]]
                batsman_name = over_stat['batsman']
                batsman_score = over_stat['runs']['batsman']
                Team_name = innings[i]['team']

                cricket_df = cricket_df.append({'Batsmans':batsman_name,'Team':Team_name,'Runs_Scored':batsman_score},ignore_index=True)

    runs_scored = cricket_df.groupby(['Batsmans','Team']).sum()
    return runs_scored


def balls_faced(match_code):
    yaml_content = yaml_df_conversionn(match_code)
    cricket_df = pd.DataFrame()

    for innings in yaml_content['innings']:
        for i in innings:
            for deliveries in innings[i]['deliveries']:
                overs = list(deliveries)[0]
                balls = str(overs).split('.')[0]
                over_stat = deliveries[list(deliveries)[0]]
                batsman_name = over_stat['batsman']
                Team_name = innings[i]['team']

                cricket_df = cricket_df.append({'Batsmans':batsman_name,'Team':Team_name,'Balls_Faced':int(balls)},ignore_index=True)

    balls_faced = cricket_df.groupby(['Batsmans','Team']).sum()
    return balls_faced


def balls_bowled(match_code):
    yaml_content = yaml_df_conversionn(match_code)
    cricket_df = pd.DataFrame()

    for innings in yaml_content['innings']:
        for i in innings:
            for deliveries in innings[i]['deliveries']:
                overs = list(deliveries)[0]
                balls = str(overs).split('.')[0]
                over_stat = deliveries[list(deliveries)[0]]
                bowler_name = over_stat['bowler']
                Team_name = innings[i]['team']

                cricket_df = cricket_df.append({'Bowler':bowler_name,'Team':Team_name,'Balls_Faced':int(balls)},ignore_index=True)

    balls_bowled = cricket_df.groupby(['Bowler','Team']).sum()
    return balls_bowled


def runs_conceded(match_code):
    yaml_content = yaml_df_conversionn(match_code)
    runs_conced = 0
    cricket_df = pd.DataFrame()
    for innings in yaml_content['innings']:
        for i in innings:
            for deliveries in innings[i]['deliveries']:
                over_stat = deliveries[list(deliveries)[0]]
                if 'extras' in over_stat:
                    bowler_name = over_stat['bowler']
                    Team_name = innings[i]['team']
                    if 'legbyes' in over_stat['extras']:
                        runs_conced = over_stat['extras']['legbyes'] + runs_conced
                    if 'wides' in over_stat['extras']:
                        runs_conced = over_stat['extras']['wides'] + runs_conced
                    if 'byes' in over_stat['extras']:
                        runs_conced = over_stat['extras']['byes'] + runs_conced

            cricket_df = cricket_df.append({'Bowler':bowler_name,'Team':Team_name,'Runs_Conceded':runs_conced},ignore_index=True)

    Runs_Conceded = cricket_df.groupby(['Bowler','Team']).sum()
    return Runs_Conceded


def get_teams(match_code):
    yaml_content = yaml_df_conversionn(match_code)

    return yaml_content['info']['teams']


def get_first_batsman(match_code):
    yaml_content = yaml_df_conversionn(match_code)



    for innings in yaml_content['innings']:
        for i in innings:
            for deliveries in innings[i]['deliveries']:
                over_stat = deliveries[list(deliveries)[0]]
                batsman_name = over_stat['batsman']

                cricket_df = pd.Series(batsman_name)

    return cricket_df[0]


def get_winner(match_code):
    yaml_content = yaml_df_conversionn(match_code)

    return yaml_content['info']['outcome']['winner']


runs_conceded(335982)
