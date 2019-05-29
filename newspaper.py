#!/usr/bin/env python3
# 
# A buggy web service in need of a database.
from flask import Flask, request, redirect, url_for

from newsdb import get_arts, get_authors, get_days

app = Flask(__name__)

# Database code for the DB Forum, full solution!

import psycopg2

DBNAME = "news"

def get_arts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select articles.title , exp2.views from(select split_part(path, '/', 3) as slug, count(time) as views from log where path like '/article/%' group by slug order by views desc limit 3) as exp2 inner join articles on articles.slug=exp2.slug")
  arts = c.fetchall()
  db.close()
  return arts
  
def get_authors():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select authors.name, sum(exp1.views) from (select articles.id, articles.title , exp2.views, articles.author as aid, exp2.slug from(select split_part(path, '/', 3) as slug, count(time) as views from log where path like '/article/%' group by slug order by views desc) as exp2 inner join articles on articles.slug=exp2.slug) as exp1 inner join authors on authors.id=exp1.aid group by authors.id order by sum(exp1.views) desc") 
  authors = c.fetchall()  
  db.close()
  return authors

def get_days():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select (to_char(log.time, 'Month DD, YYYY')) as day, (count(exp1.ref)/100) as error from(select time, count(id)*0.01 as ref from log group by time) as exp1 inner join log on log.time=exp1.time where status not like '200 OK' group by day order by (count(exp1.ref)/100) limit 1") 
  days = c.fetchall()  
  db.close()
  return days

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>NewsPaper Reporting Tool</title>
    <style>
      h1{text-align: center; }
     p{text-align: left; font-weight: bold; padding: 20px, 20px; margin: 10px 20%%; font-size:20px; } 
      div.post {margin: 10px 20%%; }        
      hr{border: 1px solid #999;
          width: 50%%; }
          </style>
  </head>
  <body>
    <h1>NewsPaper Reporting Tool</h1>
    <hr>
    <p>1. What are the most popular three articles of all time?</p>
    %s
    <br>
    <p>2. Who are the most popular article authors of all time?</p>
    %s
   <br> 
    <p>3.On which days did more than 1 &#37 of requests lead to errors?</p>
    %s
    
    </body>
</html>
'''

# HTML template for an individual comment
ART = '''\
   <div class=post>
    <ul>
    <li>%s<i>--%sviews</i></li>
    </ul>
    </div>   
'''
Author = '''\
   <div class=post>
    <ul>
    <li>%s<i>--%sviews</i></li>
    </ul>
    </div>   
'''
Day = '''\
   <div class=post>
    <ul>
    <li>%s<i>--%s&#37error</i></li>
    </ul>
    </div>      
'''

@app.route('/', methods=['GET'])
def main():
  '''Return all posts from the 'database', most recent first.'''
  arts = "".join(ART % (text, error) for text, error in get_arts())
  authors = "".join(Author % (name, views) for name, views in get_authors())
  days = "".join(Day % (day, error) for day, error in get_days()) 
  html = HTML_WRAP %(arts, authors, days)
  return html



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)

