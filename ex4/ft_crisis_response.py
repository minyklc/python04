#!/usr/bin/env python3

def ft_crisis_response():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    file = "lost_archive.txt"
    print(f"CRISIS ALERT: Attempting access to '{file}'...")
    try:
        with open(file, 'r') as f:
            f.read()
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, system stable")
        print()

    file = "classified_vault.txt"
    print(f"CRISIS ALERT: Attempting access to '{file}'...")
    try:
        with open(file, 'r') as f:
            f.read()
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, security maintained")
        print()

    file = "standard_archive.txt"
    print(f"ROUTINE ACCESS: Attempting access to '{file}'...")
    try:
        with open(file, 'r') as f:
            data = f.read()
            print(f"SUCCESS: Archive recovered -``{data}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    finally:
        print()

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
