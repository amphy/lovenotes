from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from ConfigParser import SafeConfigParser
import json, string, time, math, random

app = Flask(__name__)

mysql = MySQL()
parser = SafeConfigParser()

try:
  parser.read('/var/www/lovenotes/config.ini')
  app.config['MYSQL_DATABASE_USER'] = parser.get('database', 'username')
  app.config['MYSQL_DATABASE_PASSWORD'] = parser.get('database', 'password')
  app.config['MYSQL_DATABASE_DB'] = parser.get('database', 'name')
  app.config['MYSQL_DATABASE_HOST'] = parser.get('database', 'host')
  mysql.init_app(app)
except:
  print "ERROR WITH DATABASE CALL"

mysql_c = mysql.connect()
cursor = mysql_c.cursor()
#cursor.execute('SELECT match_id from urf')
#entries = cursor.fetchone()


@app.route("/")
def mainpage():
    return render_template('homepage.html', name = 0)

@app.route('/submit/', methods = ['POST'])
def submitnote():
  something = str(request.form['keys'])
  #need to store arrays in database
  data_entry = "{'keys': " + str(request.form['keys']) 
  data_entry += ", 'times': " + str(request.form['times']) + "}"
  #need to generate a url/random identifier and store with arrays
  keyed = uniqid()
  try:
    cursor.execute('INSERT INTO notes VALUES (%s, %s)', (keyed, data_entry))
  
    mysql_c.commit()
    #redirect to a new page with identifier
    return redirect(url_for('shownote', key=keyed))
  except:
   mysql_c.rollback()
   return "failed"

@app.route('/note/<key>')
def shownote(key):
  something = key
  #this method goes to mysql database and pulls data
  cursor.execute('SELECT data FROM notes WHERE id=(%s)', [key])
  things = cursor.fetchone()
  things = json.dumps(things)
  #b = json.loads(str(things[0]))
  print things
  #then sends it to javascript to render on page
  return render_template('submitted.html', name = something)

def uniqid(prefix='', more_entropy=False):
  m = time.time()
  uniqid = '%8x%05x' % (math.floor(m), (m-math.floor(m))*100000)
  if more_entropy:
    valid_chars = list(set(string.hexdigits.lower()))
    entropy_string = ''
    for i in range(0, 10, 1):
      entropy_string += random.choice(valid_chars)
    uniqid = uniqid + entropy_string
  uniqid = prefix + uniqid
  return uniqid

if __name__ == "__main__":
    app.run()
