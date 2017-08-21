#The flask code that sets up the database
from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

#The page that gets loaded at the beinning
@app.route('/')
def home():
   return render_template('home.html')
#This loads the data input form if the hyperlink /enternew is clicked on in home
@app.route('/enternew')
def new_student():
   return render_template('student.html')

#This takes the input from the form and writes it to the database table called student
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
        
         with sql.connect("database.db") as con:
             cur = con.cursor()
             cur.execute('''INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)''',(nm,addr,city,pin) )
             con.commit()
         msg = "Record successfully added"    
                
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()
#This returns the results of the data inputs using list.html
@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
