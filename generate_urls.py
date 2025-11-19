import random

# Number of URLs to generate
desired_url_count = 20

# Output file name
output_file_name = "threat_urls.txt"


def generate_urls(url_count):
    """
    Generator function to yield random URLs

    Args:
        url_count (int): Number of URLs to generate
    """
    for _ in range(url_count):
        yield random.choice(["http", "https"]) + "://" + "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz")
            for _ in range(random.randint(4, 16))
        ) + "." + "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz")
            for _ in range(random.randint(3, 5))
        )


# Write generated URLs to given file
with open(output_file_name, "w") as f:
    for url in generate_urls(desired_url_count):
        f.write(url + "\n")
