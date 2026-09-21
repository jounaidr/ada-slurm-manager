from src.constants import (
    PORT,
    SLURM_API_URL,
    SLURM_API_VERSION,
    VERSION,
    WORKERS,
)

def main() -> None:
    print(f"Starting ada-slurm-manager version: {VERSION}")


if __name__ == "__main__":
    main()