# ada-slurm-manager

This project provides a service that automates the creation and submission of jobs to Slurm-based systems, initiated by users of the Ada platform. It also manages data transfer between Ada and the configured Slurm service.

# Slurm REST API Client

This service uses a Python client generated from `slurm-api-spec.json` using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

The generated client is committed to the repository under `slurm-rest-api-client/` and must be installed before running the service:
```bash
pip install -e ./slurm-rest-api-client/
```

## Updating the Client

If the Slurm REST API version changes, regenerate the client and reinstall:
```bash
openapi-python-client generate --path=slurm-api-spec.json --overwrite
```

If the API version has changed (e.g. `v0037` → `v0039`), update the version-specific imports in `src/clients/slurm.py` to match the new model names.

# System Design

<img width="2008" height="2280" alt="image" src="https://github.com/user-attachments/assets/100ea380-c6d7-4c91-a278-d6322b946212" />
