# class Bird:
#     def fly(self):
#         return "Flying..."
#
# class Sparrow(Bird):
#     def fly(self):
#         return "Sparrow is flying..."
#
# class Penguin(Bird):
#     def fly(self):
#         raise Exception("Penguin cannot fly...")
#
# def make_bird_fly(bird: Bird):
#     print(bird.fly())
#
#
# sparrow = Sparrow()
# penguin = Penguin()
#
# make_bird_fly(sparrow)
# make_bird_fly(penguin)


from abc import ABC, abstractmethod

class Bird(ABC):
        pass

class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        print("Flying...")

class Sparrow(FlyingBird):
    def fly(self):
        return "Sparrow is flying..."

class Penguin(Bird):
    def swim(self):
        return "Penguin is swimming..."

def make_bird_fly(bird: FlyingBird):
    print(bird.fly())

class DB(ABC):
    @abstractmethod
    def commit(self, params):
        pass

class SQL_DB(DB):
    @abstractmethod
    def make_sql_querry(self, params):
        pass

class NOSQL_DB(DB):
    @abstractmethod
    def get_document(self, params):
        pass

class SQlite(SQL_DB):
    def commit(self, params):
        print(f"SQL query: {params}")

def save_to_db(db_instance: DB, data):
    db_instance.commit(data)

def make_query(db_instance: SQL_DB, data):
    db_instance.make_sql_querry(data)
    save_to_db(db_instance, data)

def get_document(db_instance: NOSQL_DB, data):
    db_instance.get_document(data)
    save_to_db(db_instance, data)