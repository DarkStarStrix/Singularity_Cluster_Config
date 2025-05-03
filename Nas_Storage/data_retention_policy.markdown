# Data Retention Policy

## Overview
This policy governs the storage and lifecycle of datasets, model weights, logs, and research artifacts in the Singularity Cluster’s NAS.

## Retention Rules
- **Datasets**: Retained for 5 years or until no longer needed for active projects.
- **Model Weights**: Permanent retention for trained models; archived after 2 years of inactivity.
- **Training Logs**: Retained for 3 years for debugging and reproducibility.
- **Research Artifacts**: Permanent retention, versioned in GitHub/Hugging Face.

## Deletion Process
- Automated deletion of expired data using cron jobs.
- Secure wipe (zero-fill) for sensitive datasets.

## TODO
- Implement automated lifecycle management scripts.
- Define tiered retention based on data sensitivity.
- Integrate with `raid_config.md` for storage allocation.

*See `model_hosting/model_versioning_strategy.md` for versioning details.*