import pandas as pd
import yaml
def load_data(match_code):
    with open('./files/'+str(match_code)+'.yaml','r') as f:
        doc = yaml.load(f)

    df = pd.DataFrame()
    for inn in doc['innings']:
        for i in inn:
            for this_ball in inn[i]['deliveries']:
                non_boundary = wides = legbyes = noballs = byes = penalty = wicket_kind = player_out = wicket_fielders = None
                over = str(list(this_ball)[0])
                ball = over.split('.')[1]
                over = over.split('.')[0]
                ball_det = this_ball[list(this_ball)[0]]
                batsman = ball_det['batsman']
                bowler = ball_det['bowler']
                non_striker = ball_det['non_striker']
                runs_bat = ball_det['runs']['batsman']
                if 'non_boundary' in ball_det['runs']:
                    non_boundary = ball_det['runs']['non_boundary']
                if 'extras' in ball_det:
                    if 'wides' in ball_det['extras']:
                        wides = ball_det['extras']['wides']
                    elif 'legbyes' in ball_det['extras']:
                        legbyes = ball_det['extras']['legbyes']
                    elif 'noballs' in ball_det['extras']:
                        noballs = ball_det['extras']['noballs']
                    elif 'byes' in ball_det['extras']:
                        byes = ball_det['extras']['byes']
                    if 'penalty' in ball_det['extras']:
                        penalty = ball_det['extras']['penalty']
                if 'wicket' in ball_det:
                    wicket_kind = ball_det['wicket']['kind']
                    player_out = ball_det['wicket']
                    if 'fielders' in ball_det['wicket']:
                        wicket_fielders = '/'.join(ball_det['wicket']['fielders'])

                df = df.append({'match_code':match_code,'inn': i, 'team':inn[i]['team'], 'over': over, 'ball': ball, 'batsman': batsman,
                                'bowler': bowler, 'non_striker': non_striker, 'byes': byes, 'legbyes': legbyes, 'wides': wides,
                                'noballs': noballs, 'runs_bat': runs_bat, 'non_boundary': non_boundary, 'penalty': penalty,
                                'player_out': player_out, 'wicket_kind': wicket_kind, 'wicket_fielders': wicket_fielders}, ignore_index=True)

    df['runs_total'] = df[['runs_bat','byes','legbyes','wides','noballs','penalty']].apply(pd.to_numeric).sum(axis=1)
    return [df,doc['info']]

def runs_scored(match_code):
    df = load_data(match_code)[0]
    runs_scored = df[['runs_bat','team','batsman']].apply(pd.to_numeric, errors='ignore').groupby(['batsman','team'])['runs_bat'].sum().rename('Runs_Scored').reset_index()
    return runs_scored


def balls_faced(match_code):
    df = load_data(match_code)[0]
    balls_faced = df.loc[pd.isnull(df['wides']), :].groupby(['batsman','team'])['inn'].count().rename('Balls_Faced').reset_index()
    return balls_faced

def balls_bowled(match_code):
    df = load_data(match_code)[0]
    balls_bowled = df.loc[(pd.isnull(df['wides'])) & (pd.isnull(df['noballs'])), ['bowler','team']].groupby(['bowler','team'])['bowler'].count().rename('Balls_Bowled').reset_index()
    return balls_bowled

def runs_conceded(match_code):
    df = load_data(match_code)[0]
    runs_conceded = df.loc[(pd.isnull(df['wides'])) & (pd.isnull(df['noballs'])), ['bowler','team']].groupby(['bowler','team'])['bowler'].count().rename('Balls_Bowled').reset_index()
    return runs_conceded

def get_teams(match_code):
    info = load_data(match_code)[1]
    return info['teams']

def get_first_batsman(match_code):
    df = load_data(match_code)[0]
    return df.iloc[0,df.columns.get_loc('batsman')]

def get_winner(match_code):
    info = load_data(match_code)[1]
    return info['outcome']['winner']
