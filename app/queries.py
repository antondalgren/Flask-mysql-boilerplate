import database as db


def get_users():
    query = "SELECT * FROM users"
    return db.query_db(query)
