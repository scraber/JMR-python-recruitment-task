import hashids

hasher = hashids.Hashids()


def hash_id(idx: int) -> str:
    """Auxiliary method for hashing object ID

    Args:
        idx (int): Id of object

    Returns:
        str: Hashed ID
    """
    return hasher.encode(idx)
