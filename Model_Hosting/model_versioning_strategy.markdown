# Model Versioning Strategy

## Overview
Models trained in the Singularity Cluster are versioned and hosted on GitHub and Hugging Face for open-source access.

## Versioning Process
- **Repository Structure**: Separate repos for each model family.
- **Version Tags**: Semantic versioning (e.g., v1.0.0) for weights and configs.
- **Metadata**: Training logs, hyperparameters, and evaluation metrics stored alongside weights.

## Hosting
- **GitHub**: Primary storage for model weights and documentation.
- **Hugging Face**: Public-facing hub for model discovery and fine-tuning.
- **Local NAS**: Backup of all models and artifacts.

## TODO
- Automate versioning with CI/CD pipelines.
- Implement access controls for pre-release models.
- Add documentation for model usage and fine-tuning.

*See `research_distribution.md` for distribution details.*