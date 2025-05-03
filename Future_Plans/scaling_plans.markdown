# Scaling Plans

## Overview
The Singularity Cluster is designed for incremental scalability to support billion-parameter models and beyond.

## Scaling Strategies
1. **Compute**: Add GPU/CPU nodes to the compute layer.
2. **Storage**: Expand NAS with additional drives and RAID arrays.
3. **Networking**: Deploy new nodes with 10GbE connectivity.
4. **Coordination**: Enhance Scala-based distributed systems for multi-node tasks.

## Milestones
- **Year 1-2**: Train million-parameter models, optimize AutoAPI.
- **Year 3**: Enable multi-node coordination, fault-tolerant pipelines.
- **Year 4+**: Train multi-billion parameter models, establish research hub.

## TODO
- Document hardware procurement plans.
- Benchmark scalability limits.
- Plan for cross-regional node deployment.

*See `multi-node_coordination.md` for distributed system details.*