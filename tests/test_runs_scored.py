from unittest import TestCase
import pandas as pd


class TestRuns_scored(TestCase):
    def test_runs_scored(self):
        from build import runs_scored
        df = runs_scored(335982)
        self.assertTrue(isinstance(df, pd.DataFrame))

    def test_balls_faced(self):
        from build import balls_faced
        df = balls_faced(335982)
        self.assertTrue(isinstance(df, pd.DataFrame))

    def test_balls_bowled(self):
        from build import balls_bowled
        df = balls_bowled(335982)
        self.assertTrue(isinstance(df, pd.DataFrame))

    def test_runs_conceded(self):
        from build import runs_conceded
        df = runs_conceded(335982)
        self.assertTrue(isinstance(df, pd.DataFrame))

    def test_get_teams(self):
        from build import get_teams
        df = get_teams(335982)
        self.assertTrue(isinstance(df, list))

    def test_get_first_batsman(self):
        from build import get_first_batsman
        df = get_first_batsman(335982)
        self.assertTrue(isinstance(df, str))

    def test_get_winner(self):
        from build import get_winner
        df = get_winner(335982)
        self.assertTrue(isinstance(df, str))