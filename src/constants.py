from src.config import load_config


config = load_config()

# ada-slurm-manager API
WORKERS = config.asm_api_workers
VERSION = config.asm_api_version
PORT = config.asm_api_port

# slurm REST client
SLURM_API_URL = config.slurm_api_url
SLURM_API_VERIFY_SSL = config.slurm_api_verify_ssl
