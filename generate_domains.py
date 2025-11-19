import random

# Number of domains to generate
desired_domain_count = 20

# Output file name
output_file_name = "threat_domains.txt"


def generate_domains(domain_count):
    """
    Generator function to yield random domains

    Args:
        domain_count (int): Number of domains to generate
    """
    for _ in range(domain_count):
        yield "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz")
            for _ in range(random.randint(4, 16))
        ) + "." + "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz")
            for _ in range(random.randint(3, 5))
        )


# Write generated domains to given file
with open(output_file_name, "w") as f:
    for domain in generate_domains(desired_domain_count):
        f.write(domain + "\n")
