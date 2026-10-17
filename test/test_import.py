import mysql.connector as mysql_connector

from main import MySQL


def test_import():
    imported_sql = MySQL()
    assert imported_sql.string == mysql_connector.STRING
