import sqlite3
import csv
from collections import defaultdict

#This code reads a csv file into an sql database. In this case the csv is a set of Tweet data

ifile  = open('csvfilepath.csv', "rb")
reader =  csv.DictReader(ifile)


conn = sqlite3.connect('dbfilepath.db')
conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore') #This sorts out a problem that sqlite has with 8-bit bytestrings
#the lambda function sets the coding of the string to utf-8 or ignores it
c=conn.cursor()


lst=[]		
for j, row in enumerate(reader): 
  lst.append([row['tweetid'],row['lon'], row['lat'],str(row['tweettxt']), row['created'], row['retweet_count'], row['retweeted'],row['userid'], row['userlang'],str(row['screen_name'])])
  if j % 10000 == 0:
    c.executemany('''INSERT INTO Londontweet11056test(tweetid , lon, lat, tweettxt, created,retweet_count, retweeted,userid,userlang, screen_name) values(?,?,?,?,?,?,?,?,?,?)''',lst)
    conn.commit()
    lst=[] #resets the list
  elif j==len(stored):
    c.executemany('''INSERT INTO Londontweet11056test(tweetid , lon, lat, tweettxt, created,retweet_count, retweeted,userid,userlang, screen_name) values(?,?,?,?,?,?,?,?,?,?)''',lst)
    conn.commit()
conn.close()


