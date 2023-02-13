


def connect_db (database):
    """
    Connect with your database in MongoDB
    """
    client = MongoClient("localhost:27017")
    db = client["Ironhack"]
    return db.get_collection(f"{database}")