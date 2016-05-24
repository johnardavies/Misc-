#Takes two database tables in separate databases and merges them into a single table in a new database

import sqlite3
import csv
from collections import defaultdict
from glob import glob; from os.path import expanduser

#This code takes two sql tables in separate databases and merges them in a new sql database in a single table
#The data is Tweet data

###########################################################################################################################################################
#1.Create a new database that the data will be written to
conn = sqlite3.connect('filepath\\Londontweetsintegrated230516.db')

c=conn.cursor()
#Creates a new table to store the data in the database that has just been created
c.execute('''CREATE TABLE Londontweet230516
       (tweetid text,lon real, lat real, tweettxt text, created text, retweet_count real, retweeted text,userid text,userlang text, screen_name text)''')

###########################################################################################################################################################
#2. Script that reads the pre-existing database tables into the new database
#The sql script below attaches the 3 databases and reads them Londontweetsintegrated3 and Londontweets2 into the new database Londontweetsintegrated230516.
#The table column structure is the same across all three databases#

script = '''
ATTACH "filepath\\Londontweetsintegrated230516.db" As cmaster;
ATTACH "filepath\\Londontweetsintegrated3.db" As conns2;
ATTACH "filepath\\Londontweets2.db" As conns;
INSERT INTO cmaster.Londontweet230516 SELECT * FROM conns.Londontweet020416test;
INSERT INTO cmaster.Londontweet230516 SELECT * FROM conns2.Londontweet11056testdedup;
'''


c.executescript(script) #executes the script above

conn.close()



                        


