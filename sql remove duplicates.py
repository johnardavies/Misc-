import sqlite3
import csv
from collections import defaultdict


#This connectes to a database of Tweet data
#creates a new table (Londontweet230516testdedup)
#removes duplicates from the existing table (Londontweet230516) with SELECT DISTINCT 
#and puts the deduplicated data back in the new table

conn = sqlite3.connect('filepath\\Londontweetsintegrated230516v3.db')

conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore') #This sorts out a problem that sqlite has with 8-bit bytestrings
#the lambda function sets the coding of the string to utf-8 or ignores
c=conn.cursor()

c.execute('''CREATE TABLE Londontweet230516testdedup
       (tweetid text,lon real, lat real, tweettxt text, created text, retweet_count real, retweeted text,userid text,userlang text, screen_name text)''')

script = ''' INSERT INTO Londontweet230516testdedup(tweetid , lon, lat, tweettxt, created,retweet_count, retweeted,userid,userlang, screen_name)
SELECT DISTINCT Londontweet230516.tweetid , Londontweet230516.lon, Londontweet230516.lat, Londontweet230516.tweettxt, Londontweet230516.created,Londontweet230516.retweet_count, Londontweet230516.retweeted,Londontweet230516.userid,Londontweet230516.userlang,Londontweet230516.screen_name FROM Londontweet230516
'''

c.executescript(script)
conn.close()
