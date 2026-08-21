# ada-slurm-manager

This project provides a service that automates the creation and submission of jobs to Slurm-based systems, initiated by users of the Ada platform. It also manages data transfer between Ada and the configured Slurm service.

# Slurm REST API Client

This service requires a python based slurmrestd client which is generated using the OpenAPI specification slurm-api-spec.json. This can be done by running the following:
`openapi-python-client generate --path=slurm-api-spec.json --output-path=../src/clients/slurm`

# System Design

<img width="2008" height="2280" alt="image" src="https://github.com/user-attachments/assets/100ea380-c6d7-4c91-a278-d6322b946212" />
