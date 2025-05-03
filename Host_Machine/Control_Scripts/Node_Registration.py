import docker
from typing import Dict

class NodeRegistrar:
    def __init__(self):
        self.docker_client = docker.from_env()
        self.registered_nodes: Dict = {}

    def generate_dockerfile(self, node_config: dict) -> str:
        # Basic Dockerfile template
        dockerfile = """
        FROM python:3.9
        WORKDIR /app
        COPY requirements.txt .
        RUN pip install -r requirements.txt
        COPY . .
        CMD ["python", "worker.py"]
        """
        return dockerfile

    def register_node(self, node_id: str, hardware_info: dict) -> bool:
        if node_id in self.registered_nodes:
            return False
        
        self.registered_nodes[node_id] = {
            "hardware": hardware_info,
            "status": "pending",
            "containers": []
        }
        return True

    def validate_hardware(self, hardware_info: dict) -> bool:
        # Basic hardware validation
        required_fields = ["cpu_cores", "gpu_count", "storage_gb"]
        return all(field in hardware_info for field in required_fields)
