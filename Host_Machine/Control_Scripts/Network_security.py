from typing import List, Dict
import hashlib

class NetworkSecurity:
    def __init__(self):
        self.authorized_nodes: Dict = {}
        self.access_tokens: Dict = {}

    def generate_node_token(self, node_id: str) -> str:
        token = hashlib.sha256(f"{node_id}:{datetime.now()}".encode()).hexdigest()
        self.access_tokens[node_id] = token
        return token

    def validate_node_token(self, node_id: str, token: str) -> bool:
        return self.access_tokens.get(node_id) == token

    def register_node_security(self, node_id: str, public_key: str):
        self.authorized_nodes[node_id] = {
            "public_key": public_key,
            "authorized": True
        }
