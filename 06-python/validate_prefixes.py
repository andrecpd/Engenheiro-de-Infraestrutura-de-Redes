#!/usr/bin/env python3
"""Validate sample IP prefixes and report overlaps. Standard library only."""
from ipaddress import ip_network

PREFIXES = [
    "10.10.10.0/24",
    "10.10.20.0/24",
    "10.10.10.128/25",  # Intentional overlap for the exercise
    "2001:db8:10::/48",
    "2001:db8:20::/48",
]


def main() -> int:
    networks = []
    for value in PREFIXES:
        try:
            networks.append(ip_network(value, strict=True))
        except ValueError as exc:
            print(f"INVALID {value}: {exc}")

    for index, left in enumerate(networks):
        for right in networks[index + 1:]:
            if left.version == right.version and left.overlaps(right):
                print(f"OVERLAP: {left} <-> {right}")

    print(f"Validated {len(networks)} valid prefix(es).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
