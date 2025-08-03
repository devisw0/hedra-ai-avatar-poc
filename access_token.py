# access_token.py
import time
import jwt

class VideoGrant:
    def __init__(self, room_join=False, room=None):
        self.room_join = room_join
        self.room = room

    def to_dict(self):
        grant = {}
        if self.room_join:
            grant["roomJoin"] = True
        if self.room:
            grant["room"] = self.room
        return grant

class AccessToken:
    def __init__(self, api_key, api_secret, identity, ttl=3600):
        self.api_key = api_key
        self.api_secret = api_secret
        self.identity = identity
        self.ttl = ttl
        self.grants = {}

    def add_grant(self, grant):
        self.grants.update(grant.to_dict())

    def to_jwt(self):
        now = int(time.time())
        payload = {
            "iss": self.api_key,
            "sub": self.api_key,
            "iat": now,
            "exp": now + self.ttl,
            "identity": self.identity,
            "video": self.grants
        }
        return jwt.encode(payload, self.api_secret, algorithm="HS256")
