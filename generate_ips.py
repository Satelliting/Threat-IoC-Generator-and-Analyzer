import random

# Number of IP addresses to generate
desired_ip_count = 100

# Output file name
output_file_name = "threat_ips.txt"


def generate_ips(ip_count):
    """
    Generator function to yield random IP addresses

    Args:
        ip_count (int): Number of IP addresses to generate
    """
    for _ in range(ip_count):
        yield ".".join(str(random.randint(0, 255)) for _ in range(4))


# Write generated IP addresses to given file
with open(output_file_name, "w") as f:
    for ip in generate_ips(desired_ip_count):
        f.write(ip + "\n")
