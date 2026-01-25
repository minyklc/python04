#!/usr/bin/env python3

def ft_vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print()

    print("SECURE EXTRACTION:")
    try:
        with open("classified_data.txt", "r") as file:
            data = file.read()
            print(data)
    except FileNotFoundError as e:
        print(e)
    print()

    print("SECURE PRESERVATION:")
    try:
        with open("security_protocols.txt", "r") as file:
            data = file.read()
            print(data)
    except FileNotFoundError as e:
        print(e)
    print("Vault automatically sealed upon completion")
    print()

    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()
