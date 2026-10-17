from typing import Any

import mysql.connector as mysql_connector


class MySQL:
    string: Any

    def __init__(self):
        self.string = mysql_connector.STRING
