# Singularity Cluster Config
This repository documents the high-level architecture and configuration skeleton for the **Singularity Cluster** — a fully self-owned, on-prem AI supercomputing system, designed for sovereign AI research, model development, and scientific advancement.

The Singularity Cluster represents:

- Decentralized scientific research without institutional oversight
- Full-stack AI and simulation infrastructure built independently
- A private internal ecosystem for high-signal researchers and creators

**Note:**  
Sensitive security details (API keys, internal networking specifics, private comms) are intentionally omitted. This repository is a high-level technical scaffold, evolving as hardware and operational layers come online.

> *Built for autonomy. Engineered for sovereignty.*

## Repository Structure

```plaintext
singularity-cluster-config/
├── README.md
├── LICENSE
├── cluster_overview.md
├── singularity_manifest.md
├── host_machine/
│   ├── control_scripts/
│   │   ├── job_scheduler.sh
│   │   ├── cluster_health_check.py
│   │   └── orchestration_notes.md
│   └── autoapi_config/
│       ├── autoapi_config.yaml
│       └── workflows.md
├── nas_storage/
│   ├── raid_config.md
│   ├── data_retention_policy.md
│   └── nvme_cache_setup.sh
├── compute_layer/
│   ├── gpu_training/
│   │   ├── training_node_config.yaml
│   │   └── gpu_cluster_setup.md
│   ├── gpu_inference/
│   │   └── inference_server_config.yaml
│   ├── cpu_training/
│   │   └── cpu_training_config.yaml
│   └── cpu_inference/
│       └── cpu_batch_config.yaml
├── networking/
│   ├── 10gbe_setup.md
│   ├── distributed_systems_notes.md
│   └── rust_cuda_notes.md
├── model_hosting/
│   ├── model_versioning_strategy.md
│   ├── research_distribution.md
│   └── trusted_node_protocol.md
├── future_expansion/
│   ├── scaling_plans.md
│   ├── multi-node_coordination.md
│   ├── fault_tolerance_roadmap.md
│   └── sovereign_research_network.md
├── internal_ecosystem/
│   ├── communication_protocols.md
│   ├── savant_card_initiative.md
│   └── license_and_access_rights.md
└── .gitignore
```

## Public Modules

- `host_machine/` — Orchestration and control layer configs.
- `nas_storage/` — Scalable storage architecture.
- `compute_layer/` — GPU/CPU training and inference server templates.
- `networking/` — Distributed compute networking notes.
- `model_hosting/` — Model storage, versioning, and trusted distribution.
- `future_expansion/` — Scaling roadmap for multi-node, multi-domain research.
- `internal_ecosystem/` — High-level private communication, collaboration, and access protocols.
