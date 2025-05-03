# 10GbE Networking Setup

## Overview
The Singularity Cluster uses 10GbE networking for low-latency, high-bandwidth communication between nodes.

## Hardware
- **Switches**: Enterprise-grade 10GbE switches (e.g., Ubiquiti UniFi).
- **NICs**: 10GbE network interface cards per node.
- **Cabling**: Cat6a or fiber for maximum performance.

## Configuration
1. Configure switches for VLAN segmentation (compute, storage, management).
2. Assign static IPs to nodes for reliability.
3. Enable jumbo frames for large data transfers.
4. Monitor network performance with tools like iperf.

## TODO
- Document specific switch models and firmware.
- Implement QoS for prioritizing training traffic.
- Add redundancy with link aggregation.

*See `distributed_systems_notes.md` for multi-node coordination.*