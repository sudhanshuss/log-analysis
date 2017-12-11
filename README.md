# log-analysis


This is a repository for log analysis project written in python language.

# Prerequisites

* Need to run with python 3.5.3 version.
* Need to run with postgres 9.6 version.
* Need psycopg2.
* Need to run against "news" schema.
* Need to create below views :
  1. CREATE VIEW articles_by_views AS SELECT title, COUNT(log.id) AS views FROM articles, log
     WHERE log.path = CONCAT('/article/',slug) GROUP BY title ORDER BY views desc;
  2. CREATE VIEW articles_by_authors AS SELECT name,title from authors,articles where authors.id=articles.author;
  3. CREATE VIEW total_articles_view AS SELECT date(time), COUNT(*) AS views
     FROM log GROUP BY date(time);
  4. CREATE VIEW error_articles_view AS SELECT date(time), COUNT(*) AS errors
     FROM log WHERE status = '404 NOT FOUND' GROUP BY date(time);
  5. CREATE VIEW error_percentage AS SELECT total_articles_view.date, 
     (100*error_articles_view.errors/total_articles_view.views) AS percentage
     FROM total_articles_view, error_articles_view WHERE total_articles_view.date = error_articles_view.date ORDER BY total_articles_view.date;
  

# Installing

git clone https://github.com/sudhanshuss/log-analysis.git

# Run the code

* load the data in database 
  * psql -d news -f newsdata.sql
* create the views as given in Prerequisites
* run command
  * python3 loganalysis.py
