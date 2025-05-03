# Fault Tolerance Roadmap

## Overview
Fault tolerance ensures the Singularity Cluster remains operational during hardware or software failures.

## Current State
- RAID 5 on NAS for storage redundancy.
- AutoAPI retries failed jobs (basic implementation).
- Manual failover for node outages.

## Roadmap
- **Year 1-2**: Implement automated node failover in AutoAPI.
- **Year 3**: Add redundant networking paths and hot spares.
- **Year 4+**: Achieve zero-downtime training for billion-parameter models.

## TODO
- Develop failover scripts for compute nodes.
- Test RAID rebuild performance.
- Integrate with `cluster_health_check.py` for proactive monitoring.

*See `raid_config.md` for storage redundancy details.*