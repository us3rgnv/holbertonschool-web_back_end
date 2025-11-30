#!/usr/bin/env python3
""" 11-schools_by_topic.py """

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic

    Args:
        mongo_collection (pymongo.collection.Collection): MongoDB collection object
        topic (str): Topic to search for

    Returns:
        list: List of documents matching the topic
    """
    if mongo_collection is None or topic is None:
        return []

    return list(mongo_collection.find({ "topics": topic }))
