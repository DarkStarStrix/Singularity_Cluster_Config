# Singularity Cluster Overview

## Purpose
The Singularity Cluster is a self-sovereign, on-prem AI supercomputing system designed for decentralized AI research, model training, and inference. It removes reliance on cloud providers, ensuring full control over compute, data, and infrastructure. This document provides a high-level overview of the Cluster’s architecture and operational principles.

## Architecture
The Cluster comprises five core layers:
1. **Host Machine (Control & Orchestration)**: Manages workflows, job scheduling, and node coordination using AutoAPI.
2. **NAS (Storage & Data Management)**: Scalable storage for datasets, model weights, and logs, with RAID and NVMe caching.
3. **Compute Layer**: GPU and CPU servers for training and inference, optimized for efficiency and scalability.
4. **Networking & Scaling**: 10GbE networking and distributed systems (Rust, CUDA, Scala) for multi-node coordination.
5. **Model Hosting & Research Distribution**: Versioned models on GitHub/Hugging Face, with open-source research outputs.

## Key Features
- **Modular Scalability**: Add compute, storage, or nodes incrementally without redesign.
- **Security**: On-prem infrastructure ensures data sovereignty and eliminates vendor lock-in.
- **Performance**: Optimized for a million to a billion-parameter models, rivaling FAANG-scale systems.
- **Decentralization**: Open-source model hosting and research distribution for global access.

## Operational Principles
- Built and maintained by a single engineer, emphasizing technical mastery.
- Designed for fault tolerance, low-latency, and high-throughput AI workloads.
- Evolving toward full AI sovereignty and a decentralized research hub.

*See `singularity_manifest.md` for philosophical context and `README.md` for repository structure.*