# Parsing YAML

The file files/335982.yaml has ball-by-ball summary of a cricket match. Produce the following simple version of match scorecard from it listing the following.

__Question 1__

Write a function that returns how many runs were scored by each batsman?

* Define a function with name runs_scored which will accept integer parameter match_code.
* According to match code find out batsmans and runs scored by them.
* Store them inside pandas dataframe which should have columns
    * Batsmans
    * Team
    * Runs_Scored
* match_code is nothing but name of yaml file. When you send match_code you should parse match_code.yaml file.
* In this scenario pass match_code as 335982 which should parse 335982.yaml file stored in files directory.


__Question 2__

Write a function that returns how many balls were faced by each batsman?

* Define a function with name balls_faced which will accept integer parameter match_code.
* According to match code find out batsmans and balls faced by them.
* Store them inside pandas dataframe which should have columns
    * Batsmans
    * Team
    * Balls_Faced
* match_code is nothing but name of yaml file. When you send match_code you should parse match_code.yaml file.
* In this scenario pass match_code as 335982 which should parse 335982.yaml file stored in files directory.


__Question 3__

Write a function that returns how many balls were balled by each bowler?

* Define a function with name balls_bowled which will accept integer parameter match_code.
* According to match code find out bowlers and balls bowled by them.
* Store them inside pandas dataframe which should have columns
    * Bowler
    * Team
    * Balls_Bowled
* match_code is nothing but name of yaml file. When you send match_code you should parse match_code.yaml file.
* In this scenario pass match_code as 335982 which should parse 335982.yaml file stored in files directory.


__Question 4__

Write a function that returns how many runs were conceded by each bowler?

* Define a function with name runs_conceded which will accept integer parameter match_code.
* According to match code find out bowlers and runs conceded by them.
* Store them inside pandas dataframe which should have columns
    * Bowler
    * Team
    * Runs_Conceded
* match_code is nothing but name of yaml file. When you send match_code you should parse match_code.yaml file.
* In this scenario pass match_code as 335982 which should parse 335982.yaml file stored in files directory.


__Question 5__

Write a function that returns name of the teams.

* Define a function with name get_teams which will accept integer parameter match_code.
* According to match code find out name of all teams.
* Store them inside list which should have team names.
* match_code is nothing but name of yaml file. When you send match_code you should parse match_code.yaml file.
* In this scenario pass match_code as 335982 which should parse 335982.yaml file stored in files directory.


__Question 6__

Write a function that returns who batted first?

* Define a function with name get_first_batsman which will accept integer parameter match_code.
* According to match code find out name of the first batsman.
* Return batsman name as string variable.
* match_code is nothing but name of yaml file. When you send match_code you should parse match_code.yaml file.
* In this scenario pass match_code as 335982 which should parse 335982.yaml file stored in files directory.


__Question 7__

Write a function that returns who won?

* Define a function with name get_winner which will accept integer parameter match_code.
* According to match code find out winner team of match.
* Return team name as string variable.
* match_code is nothing but name of yaml file. When you send match_code you should parse match_code.yaml file.
* In this scenario pass match_code as 335982 which should parse 335982.yaml file stored in files directory.
