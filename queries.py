from dbuse import UseDatabase, CredentialsError, ConnectionError, UseDatabaseDictionary

#Configuration for the Database
dbconfig = {"host": "XXXXXX",
            "user": "XXXXXX",
            "password": "XXXXXXX",
            "database": "XXXXX"}

#Select statement to retrieve website URL
def select(site, st):
  try:
      with UseDatabase(dbconfig) as cursor: 
          _SQL_select = """select WEBSITE_URL from website.site where website_url = %s"""
           cursor.execute(_SQL_select,(site,))
           data = cursor.fetchall()
           print(st + " Select executed")
           return data
   except ConnectionError as err:
        print(err)
   except CredentialsError as err:
        print(err)
   except Exception as err:
        print(err)

#Insert statement 
def insert(site, title, body_nospace, body_raw, st):
  try:
      with UseDatabase(dbconfig) as cursor: 
          _SQL_insert = """INSERT INTO website.site (WEBSITE_URL, WEBSITE_TITLE, SITE_BODY, SITE_HTML) VALUES (%s, %s, %s, %s)"""
          cursor.execute(_SQL_insert,(str(site), str(title), str(body_nospace), str(body_raw)))
          print(st + " INSERT executed")
   except ConnectionError as err:
        print(err)
   except CredentialsError as err:
        print(err)
   except Exception as err:
        print(err)

#Update the database
def update(site, title, body_nospace, body_raw, st):
  try:
       with UseDatabase(dbconfig) as cursor: 
            _SQL_update = """UPDATE website.site SET WEBSITE_TITLE = %s, SITE_BODY = %s, SITE_HTML = %s where WEBSITE_URL = %s"""
             cursor.execute(_SQL_update,(str(title), str(body_nospace), str(body_raw), site))
             print(st + " UPDATE executed")
   except ConnectionError as err:
        print(err)
   except CredentialsError as err:
        print(err)
   except Exception as err:

#Simple select for data lookup
def lookup_select():
    try:
        with UseDatabaseDictionary(dbconfig) as cursor: 
            _SQL_select = """select Website_URL,Website_title, site_body from website.site"""
            cursor.execute(_SQL_select)
            data = cursor.fetchall()
        return data
    except ConnectionError as err:
        print(err)
    except CredentialsError as err:
        print(err)
    except Exception as err:
        print(err)
