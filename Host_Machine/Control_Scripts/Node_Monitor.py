import asyncio
from datetime import datetime

class NodeMonitor:
    def __init__(self):
        self.nodes = {}
        self.health_checks = {}

    async def start_monitoring(self, node_id: str):
        self.nodes[node_id] = {
            "last_heartbeat": datetime.now(),
            "status": "online",
            "metrics": {}
        }
        asyncio.create_task(self._monitor_node(node_id))

    async def _monitor_node(self, node_id: str):
        while True:
            await self._check_node_health(node_id)
            await asyncio.sleep(60)  # Check every minute

    async def _check_node_health(self, node_id: str):
        # Implement health check logic
        pass

    def get_node_status(self, node_id: str) -> dict:
        return self.nodes.get(node_id, {"status": "unknown"})
