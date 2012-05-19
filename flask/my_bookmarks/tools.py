import hashlib
from my_bookmarks import SECRET_KEY

def hash_password(username, password):
    return hashlib.sha512(('%s%s%s'%(password,SECRET_KEY, username))).hexdigest()

