# Orchestration Notes

## Overview
The Host Machine orchestrates the Singularity Cluster using AutoAPI, a custom AI automation framework. This document outlines key considerations and TODOs for orchestration.

## Key Components
- **AutoAPI**: Manages job scheduling, resource allocation, and workflow execution.
- **Job Scheduler**: Distributes tasks across GPU/CPU compute nodes (`job_scheduler.sh`).
- **Health Monitoring**: Tracks node status and system metrics (`cluster_health_check.py`).

## Orchestration Workflow
1. Receive job requests (training, inference, preprocessing).
2. Allocate resources based on node availability and task requirements.
3. Execute tasks via AutoAPI, ensuring low-latency coordination.
4. Log results and monitor system health.

## TODO
- Implement dynamic resource allocation for multi-node tasks.
- Optimize AutoAPI for billion-parameter model training.
- Add failover mechanisms for node outages.

*See `autoapi_config/autoapi_config.yaml` for configuration details.*