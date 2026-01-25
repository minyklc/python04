#!/usr/bin/env python3

def ft_archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    data = ("[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n"
            "[ENTRY 003] Archived by Data Archivist trainee\n")
    file = "new_discovery.txt"
    print(f"Initializing new storage unit: {file}")
    f = open(file, 'w')
    print("Storage unit created successfully...")
    print()

    print("Inscribing preservation data...")
    f.write(data)
    print(data)

    f.close()
    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    ft_archive_creation()
