# generate_token.py
import os
from dotenv import load_dotenv
from access_token import AccessToken, VideoGrant

load_dotenv()

api_key    = os.getenv("LIVEKIT_API_KEY")
api_secret = os.getenv("LIVEKIT_API_SECRET")
identity   = "devan"     # any unique string
room       = "default"   # must match your agent’s room

# build token
tok = AccessToken(api_key, api_secret, identity)
tok.add_grant(VideoGrant(room_join=True, room=room))

print(tok.to_jwt())
