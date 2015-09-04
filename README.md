# Slowotok auto player

### Application to solve game named Slowotok(slowotok.pl).

Now in early stage. Needs much improvements, esp. in performance.


### How it works:
You need to have an account at slowotok.pl

You pass your login and password and then app:
1. logs in into your account
2. goes to game page
3. reads letters from game board
4. creates combinations of letters according to game rules(see below)


### Game rules
Game have a board - matrix 4x4.
Every element is a letter. 
You have to merge letters to create polish nouns.
Letters can be merged into word only if their lays in a distance of one block of each other.

#### Example board:

U D T A

B E X N 

W W B I

U V M S

Example word from this letters: T A X I


### Arguments:
-h, --help          show this help message and exit
-login LOGIN        Your login in Slowotok
-password PASSWORD  Your password in Slowotok
