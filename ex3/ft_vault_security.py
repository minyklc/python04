#!/usr/bin/env python3

def ft_vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print()

    print("SECURE EXTRACTION:")
    data = None
    try:
        with open("classified_data.txt", 'r') as file:
            data = file.read()
            print(data)
    except FileNotFoundError as e:
        print(e)
    print()

    print("SECURE PRESERVATION:")
    try:
        with open("security_protocols.txt", 'r') as file:
            data2 = file.read()
            print(data2)
        if data is None:
            raise Exception("read() error in classified_data.txt")
        with open("security_protocols.txt", 'w') as file2:
            file2.write(data)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    print("Vault automatically sealed upon completion")
    print()

    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()
