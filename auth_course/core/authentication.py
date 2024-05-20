import jwt,datetime
from rest_framework.exceptions import AuthenticationFailed

def create_access_token(id):
    return jwt.encode({
        'user_id':id,
        'exp':datetime.datetime.utcnow()+datetime.timedelta(seconds=90),  # token life 30 sec
        'iat': datetime.datetime.utcnow()     #token creation time
    },"access_secret",algorithm="HS256")  # passing the algoritm for hashing
    
def decode_access_token(token):
    try:
        payload=jwt.decode(token,'access_secret',algorithms='HS256')
        return payload["user_id"]
    except Exception as e: 
        print(e)
        raise AuthenticationFailed("Unauthenticated")

def create_refresh_token(id):
    return jwt.encode({
        'user_id':id,
        'exp':datetime.datetime.utcnow()+datetime.timedelta(days=7),  # token life 30 sec
        'iat': datetime.datetime.utcnow()     #token creation time
    },"refresh_secret",algorithm="HS256")  # passing the algoritm for hashing
