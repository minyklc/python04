#!/usr/bin/env python3
import sys


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. "
                   "Enter status report: ")
    print()

    print(f"[STANDARD] Archive status from "
          f"{id}: {status}", file=sys.stdout)
    print("[ALERT] System diagnostic: "
          "Communication channels verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stderr)
    print()

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    ft_stream_management()
