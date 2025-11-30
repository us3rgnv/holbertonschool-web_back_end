#!/usr/bin/env python3
""" 10-update_topics.py """

def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the school name

    Args:
        mongo_collection (pymongo.collection.Collection): MongoDB collection object
        name (str): School name to update
        topics (list of str): List of topics to set
    """
    if mongo_collection is None or name is None or topics is None:
        return

    mongo_collection.update_one(
        { "name": name },
        { "$set": { "topics": topics } }
    )
