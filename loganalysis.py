import psycopg2

# DataBase name
DBNAME = "news"

# Solution 1 : is  to print the top three popular article.
def popular_three_article():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = "SELECT * from articles_by_views LIMIT 3"
    c.execute(query)
    result = c.fetchall()
    db.close()
    for popular_article in result:
        print("%s --- %s views" % (popular_article[0], popular_article[1]))

#Solution 2 : is  to print the most post authors in desc order
def most_popular_author():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """select name,sum(articles_by_views.views) As views from articles_by_authors,
            articles_by_views where articles_by_authors.title =
            articles_by_views.title GROUP BY articles_by_authors.name
            ORDER BY views DESC"""
    c.execute(query)
    result = c.fetchall()
    db.close()
    for popular_author in result:
        print("%s --- %s views" % (popular_author[0], popular_author[1]))

#Solution 3 : is to print the day in which error rate was greater that 1%
def requests_lead_to_error():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """select to_char(date,'MONTH DD,YYYY'),percentage from error_percentage 
    WHERE error_percentage.percentage > 1"""		
    c.execute(query)
    result = c.fetchall()
    db.close()
    for error in result:
        print("%s --- %s %% error" % (error[0], error[1]))


if __name__ == "__main__":
    popular_three_article()
    print("-----------------------")
    most_popular_author()
    print("-----------------------")
    requests_lead_to_error()
