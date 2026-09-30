#Dependency Inversion Principle (DIP)
# High-level class যেন সরাসরি কোনো specific low-level class-এর উপর depend না করে।
# বরং দুটোই একটা abstraction-এর উপর depend করবে।

# bad design
"""
class MySQLDatabase:
    def save(self):
        print("Data saved to MySQL")

class UserService:
    def __init__(self):
        self.database = MySQLDatabase()
    def save_user(self):
        self.database.save()
"""

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self):
        pass

class MySQLDatabase(Database):
    def save(self):
        print("Data saved to MySQL")

class PostgreSQLDatabase(Database):
    def save(self):
        print("Data saved to PostgreSQL")

class UserService:
    def __init__(self, database):
        self.database = database

    def save_user(self):
        self.database.save()


mysql = MySQLDatabase()
postgresql = PostgreSQLDatabase()

user_service_1 = UserService(mysql)
user_service_1.save_user()

user_service_2 = UserService(postgresql)
user_service_2.save_user()