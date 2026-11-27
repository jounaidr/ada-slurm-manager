from src.constants import (
    PORT,
    SLURM_API_URL,
    VERSION,
    WORKERS,
)

def main() -> None:
    print(f"Starting ada-slurm-manager version: {VERSION}")


if __name__ == "__main__":
    main()