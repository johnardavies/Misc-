import csv
import sqlite3

from glob import glob; from os.path import expanduser
conn = sqlite3.connect('dbfilepath.db')

cursor = conn.cursor()

#selects the lon and lat columns from the sql table Londontweet11056testdedup
cursor.execute("select lon, lat from Londontweet11056testdedup;")

with open("csv filepath.csv", "wb") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description]) # write headers
    csv_writer.writerows(cursor)
