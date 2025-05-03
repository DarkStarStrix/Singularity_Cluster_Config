# NAS RAID Configuration

## Overview
The NAS (Network Attached Storage) layer uses RAID for fault tolerance and data integrity. This document outlines the RAID setup for the Singularity Cluster’s storage.

## RAID Configuration
- **Type**: RAID 5 (minimum 3 drives, balancing redundancy and capacity).
- **Drives**: Enterprise-grade HDDs/SSDs, hot-swappable.
- **File System**: ZFS for data integrity and snapshots.
- **NVMe Caching**: Enabled for high-speed data retrieval.

## Setup Steps
1. Initialize RAID array with `mdadm` or ZFS tools.
2. Configure NVMe cache for read/write acceleration.
3. Set up automated backups and snapshots.

## TODO
- Document specific RAID parameters (e.g., stripe size).
- Implement monitoring for drive health and rebuild status.
- Plan for RAID 6 or ZFS RAID-Z for larger arrays.

*See `nvme_cache_setup.sh` for caching configuration.*