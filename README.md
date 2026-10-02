# ada-slurm-manager

This project provides a service that automates the creation and submission of jobs to Slurm-based systems, initiated through the [Ada platform](https://ada.stfc.ac.uk/). It also manages data transfer between Ada and the Slurm service.

## Slurm REST API Client

This service uses a Python client generated from `slurm-api-spec.json` using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

The generated client is committed to the repository under `slurm-rest-api-client/` and must be installed before running the service:
```bash
pip install -e ./slurm-rest-api-client/
```

### Updating the Client

If the Slurm REST API version changes, regenerate the client and reinstall:
```bash
openapi-python-client generate --path=slurm-api-spec.json --overwrite
```

If the API version has changed (e.g. `v0037` → `v0039`), update the version-specific imports in `src/clients/slurm.py` to match the new model names.
