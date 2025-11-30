#!/usr/bin/env python3
""" 8-all.py """

def list_all(mongo_collection):
    """
    Lists all documents in a collection

    Args:
        mongo_collection (pymongo.collection.Collection): MongoDB collection object

    Returns:
        list: List of documents in the collection, empty list if none
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
