from dbuse import UseDatabase, CredentialsError, ConnectionError, UseDatabaseDictionary
import json

#Configuration for the Database stored in a JSON file
with open("dbconfig.json", "r") as file:
    data = json.loads(file.read())
    dbconfig = data["dbconfig"]

# select statement used in lookup and read CSV. ID is an identifier exactly where we use it. If ID = 1 we are executing the SELECT from readcsv
# If = 0 we use the SELECT statement from the lookup
def select(site, st, _SQL_select, ID):
    try:
        if ID == 1: 
            with UseDatabase(dbconfig) as cursor:
                cursor.execute(_SQL_select,(site,))
                data = cursor.fetchall()
                print(st + " Select executed")
            return data
        else:
            with UseDatabaseDictionary(dbconfig) as cursor:
                cursor.execute(_SQL_select)
                data = cursor.fetchall()
            return data
    except ConnectionError as err:
        print(err)
    except CredentialsError as err:
        print(err)
    except Exception as err:
        print(err)

#Insert/update statement 
def insert_update(site, title, body_nospace, body_raw, st, _SQL, p):
    try:
        with UseDatabase(dbconfig) as cursor:
            cursor.execute(_SQL,(str(site), str(title), str(body_nospace), str(body_raw)))
            print(st + " " + str(p))
    except ConnectionError as err:
        print(err)
    except CredentialsError as err:
        print(err)
    except Exception as err:
        print(err)


