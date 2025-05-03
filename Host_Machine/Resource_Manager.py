from typing import Dict, List

class ResourceManager:
    def __init__(self):
        self.resources: Dict = {}
        self.allocated_resources: Dict = {}

    def add_node_resources(self, node_id: str, resources: dict):
        self.resources[node_id] = resources

    def allocate_resources(self, request_id: str, requirements: dict) -> bool:
        # Basic resource allocation logic
        available_nodes = self._find_available_nodes(requirements)
        if not available_nodes:
            return False
        
        self.allocated_resources[request_id] = {
            "nodes": available_nodes,
            "requirements": requirements
        }
        return True

    def _find_available_nodes(self, requirements: dict) -> List[str]:
        # Simple node matching logic
        matching_nodes = []
        for node_id, resources in self.resources.items():
            if self._check_resource_availability(resources, requirements):
                matching_nodes.append(node_id)
        return matching_nodes
