#!/usr/bin/env python3
import os
import time
import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
from access_token import AccessToken, VideoGrant

load_dotenv()

class TokenHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/generate-token':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            # Generate fresh token
            api_key = os.getenv("LIVEKIT_API_KEY")
            api_secret = os.getenv("LIVEKIT_API_SECRET")
            identity = "devan"
            room = "default"
            
            tok = AccessToken(api_key, api_secret, identity, ttl=3600)  # 1 hour
            tok.add_grant(VideoGrant(room_join=True, room=room))
            token = tok.to_jwt()
            
            print(f"🔑 Generated fresh token at {time.strftime('%H:%M:%S')}")
            print(f"Token ends with: {token[-20:]}")
            
            self.wfile.write(token.encode())
            return
        
        # Serve static files normally
        super().do_GET()

if __name__ == "__main__":
    PORT = 9999
    print(f"🚀 Starting token server on http://localhost:{PORT}")
    print(f"🔑 Token endpoint: http://localhost:{PORT}/generate-token")
    print(f"📁 Nuclear page: http://localhost:{PORT}/public/nuclear.html")
    
    with socketserver.TCPServer(("", PORT), TokenHTTPRequestHandler) as httpd:
        httpd.serve_forever()
