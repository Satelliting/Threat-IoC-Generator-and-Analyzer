import random

from dataclasses import dataclass


# Number of IoCs to generate
desired_ioc_count = 500

# Output file name
ioc_file_name = "threat_iocs.txt"

# List of potential IoC types (3 total)
ioc_types = ["ip", "domain", "url"]

# Boolean to determine if IP file should be utilized
use_ip_file = True

# Boolean to determine if Domain file should be utilized
use_domain_file = True

# Boolean to determine if URL file should be utilized
use_url_file = True

# List of potential actors (9 total)
actors = [
    "attacker",
    "malware",
    "botnet",
    "ransomware",
    "scam",
    "spyware",
    "trojan",
    "virus",
    "worm",
]


@dataclass
class IoC:
    """
    Dataclass to store IoC information
    """

    type: str  # Type of IoC (e.g., IP, Domain, URL)
    value: str  # IP Address, Domain, or URL
    actor: str  # Actor or Group


def generate_ip_for_ioc():
    """
    Generator function to yield random IP addresses for IoCs
    """
    if use_ip_file:
        with open("threat_ips.txt", "r") as f:
            yield random.choice(f.readlines()).strip()
    else:
        yield ".".join(str(random.randint(0, 255)) for _ in range(4))


def generate_domain_for_ioc():
    """
    Generator function to yield random domains for IoCs
    """
    if use_domain_file:
        with open("threat_domains.txt", "r") as f:
            yield random.choice(f.readlines()).strip()
    else:
        yield "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz")
            for _ in range(random.randint(4, 16))
        ) + "." + "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz")
            for _ in range(random.randint(3, 5))
        )


def generate_url_for_ioc():
    """
    Generator function to yield random URLs for IoCs
    """
    if use_url_file:
        with open("threat_urls.txt", "r") as f:
            yield random.choice(f.readlines()).strip()
    else:
        yield random.choice(["http", "https"]) + "://" + "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz")
            for _ in range(random.randint(4, 16))
        ) + "." + "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz")
            for _ in range(random.randint(3, 5))
        )


def generate_iocs(ioc_count):
    """
    Generator function to yield random IoCs

    Args:
        ioc_count (int): Number of IoCs to generate
    """
    for _ in range(ioc_count):
        ioc_type = random.choice(ioc_types)
        ioc_value = None

        if ioc_type == "ip":
            ioc_value = next(generate_ip_for_ioc())
        elif ioc_type == "domain":
            ioc_value = next(generate_domain_for_ioc())
        elif ioc_type == "url":
            ioc_value = next(generate_url_for_ioc())

        actor = random.choice(actors)

        yield IoC(ioc_type, ioc_value, actor)


# Write generated IoCs to given file
with open(ioc_file_name, "w") as f:
    for ioc in generate_iocs(desired_ioc_count):
        f.write(f"{ioc.type},{ioc.value},{ioc.actor}\n")
