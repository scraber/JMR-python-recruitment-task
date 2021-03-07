import hashids
from django.conf import settings

hasher = hashids.Hashids(salt=settings.HASHID_SALT)


def hash_id(idx: int) -> str:
    """Auxiliary method for hashing object ID

    Args:
        idx (int): Id of object

    Returns:
        str: Hashed ID
    """
    return hasher.encode(idx)
