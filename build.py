import yaml, pandas as pd
def create_df(match_code):
    with open("./files/"+str(match_code)+".yaml", 'r') as stream:
        yaml_obj = yaml.load(stream)
    final_list = []
    for inning in yaml_obj['innings']:
        for inn, i in inning.items():
            rows = i['deliveries']
            for x in rows:
                row_items = {}
                row_items['ball no'] = x.keys()[0]
                for ball in x.values():
                    row_items['batsman'] = ball['batsman']
                    row_items['bowler'] = ball['bowler']
                    row_items['non_striker'] = ball['non_striker']
                    row_items['runs_scored'] = ball['runs']['batsman']
                    row_items['total runs'] = ball['runs']['total']
                    row_items['extra'] = ball['runs']['extras']
                    row_items['team'] = i['team']
                    row_items['innings'] = inn
                    final_list.append(row_items)
    df = pd.DataFrame(final_list)
    return df



def runs_scored(match_code):
    with open("./files/"+str(match_code)+".yaml", 'r') as stream:
        yaml_obj = yaml.load(stream)
    final_list = []
    for inning in yaml_obj['innings']:
        for inn, i in inning.items():
            rows = i['deliveries']
            for x in rows:
                row_items = {}
                row_items['ball no'] = x.keys()[0]
                for ball in x.values():
                    row_items['batsman'] = ball['batsman']
                    row_items['bowler'] = ball['bowler']
                    row_items['non_striker'] = ball['non_striker']
                    row_items['runs_scored'] = ball['runs']['batsman']
                    row_items['total runs'] = ball['runs']['total']
                    row_items['extra'] = ball['runs']['extras']
                    row_items['team'] = i['team']
                    row_items['innings'] = inn
                    final_list.append(row_items)
    df = pd.DataFrame(final_list)
    df1 = df.loc[:,['batsman','team','runs_scored']]
    df2 = df1.groupby(['batsman','team']).sum()
    return df2


def balls_faced(match_code):
    df = create_df(match_code)
    df4 = df.loc[:,['batsman','ball no','team']].groupby(['batsman','team']).count()
    df4.rename(columns={'ball no': 'Balls_Faced'}, inplace=True)
    return df4

def balls_bowled(match_code):
    df = create_df(match_code)
    df3 = df.loc[:,['bowler','ball no','team']].groupby(['bowler','team']).count()
    df3.rename(columns={'bowler':'Bowler','ball no': 'Balls_Bowled','team':'Team'}, inplace=True)
    return df3


def runs_conceded(match_code):
    df = create_df(match_code)
    df5 =  df.loc[:,['bowler','total runs','team']].groupby(['bowler','team']).sum()
    df5.rename(columns={'total runs': 'Runs_Conceded'}, inplace=True)
    return df5


def get_teams(match_code):
    with open("./files/"+str(match_code)+".yaml", 'r') as stream:
        yaml_obj = yaml.load(stream)
    return yaml_obj['info']['teams']

def get_first_batsman(match_code):
    df = create_df(match_code)
    return df[(df['ball no']==0.1) & (df['innings']=='1st innings')]['batsman'][0]


def get_winner(match_code):
    with open("./files/"+str(match_code)+".yaml", 'r') as stream:
        yaml_obj = yaml.load(stream)
    return yaml_obj['info']['outcome']['winner']
