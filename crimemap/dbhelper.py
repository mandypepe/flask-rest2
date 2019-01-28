import pymysql
import db_cfg.dbconfig as dbconfig
import datetime
import dateparser


class DBHelper:
    def connect(self, database="crimemap"):
        return pymysql.connect(host='localhost',user=dbconfig.db_user,passwd=dbconfig.db_password,db=database)

    def get_all_inputs(self):
        connection = self.connect()
        named_crimes = []
        try:
            query = "SELECT * FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            for crime in cursor:
                named_crime = {
                    'id':crime[0],
                    'latitude': crime[1],
                    'longitude': crime[2],
                    'date': datetime.datetime.strftime(crime[3], '%Y-%m-%d'),
                    'category': crime[4],
                    'description': crime[5]
                }
                named_crimes.append(named_crime)
            return named_crimes
        finally:
            connection.close()

    def format_date(userdate):
        date = dateparser.parse(userdate)
        try:
            return datetime.datetime.strftime(date, "%Y-%m-%d")
        except TypeError:
            return None

    def add_input(self, data):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (description) VALUES ('{}'); ".format(data)
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
                connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()
