#!/usr/bin/env python3

def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    file = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {file}")
    try:
        f = open(file, 'r')
        print("Connection established...")
        print()
        print("RECOVERED DATA:")
        print(f.read())
        f.close()
        print()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")


if __name__ == "__main__":
    ft_ancient_text()
