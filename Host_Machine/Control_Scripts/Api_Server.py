from fastapi import FastAPI, Request
from pydantic import BaseModel
import os
import psutil

app = FastAPI()

# In-memory node registry (replace with DB in production)
node_registry = {}

class NodeRegistration(BaseModel):
    node_id: str
    cpu_cores: int = 0
    gpu_count: int = 0
    storage_gb: int = 0
    cpu_commit: int
    gpu_commit: int
    storage_commit: int

@app.post("/register_node")
def register_node(reg: NodeRegistration):
    # Add node to registry
    node_registry[reg.node_id] = {
        "cpu_cores": reg.cpu_cores,
        "gpu_count": reg.gpu_count,
        "storage_gb": reg.storage_gb,
        "cpu_commit": reg.cpu_commit,
        "gpu_commit": reg.gpu_commit,
        "storage_commit": reg.storage_commit,
        "status": "registered"
    }
    # TODO: Generate Dockerfile and send to node
    return {"status": "registered", "node_id": reg.node_id}

@app.get("/inspect")
def inspect():
    # Example: gather local hardware info
    cpu_cores = os.cpu_count()
    storage = psutil.disk_usage('/').total // (1024 ** 3)
    # TODO: Add GPU detection
    return {"cpu_cores": cpu_cores, "storage_gb": storage}

@app.post("/commit_compute/{node_id}")
def commit_compute(node_id: str):
    # Mark node as committed
    if node_id in node_registry:
        node_registry[node_id]["status"] = "committed"
        # TODO: Start monitoring
        return {"status": "committed"}
    return {"error": "node not found"}

@app.get("/nodes")
def list_nodes():
    return node_registry

class FederatedTrainingConfig(BaseModel):
    model_type: str
    dataset_path: str
    num_rounds: int
    min_nodes: int

@app.post("/federated_training")
async def start_federated_training(config: FederatedTrainingConfig):
    # Initialize federated training job
    return {"job_id": "fed_train_1", "status": "initialized"}

@app.post("/distributed_compute")
async def submit_distributed_job(job: dict):
    # Handle distributed compute job submission
    return {"job_id": "dist_1", "status": "submitted"}

@app.get("/job_status/{job_id}")
async def get_job_status(job_id: str):
    # Get status of running jobs
    return {"job_id": job_id, "status": "running"}
