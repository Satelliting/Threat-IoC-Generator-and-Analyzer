from generate_iocs import IoC, ioc_file_name
from collections import defaultdict, Counter


def stream_iocs(file_name):
    """
    Generator function to yield IoCs from a file

    Args:
        file_name (str): Name of the file containing IoCs
    """
    with open(file_name, "r") as f:
        for line in f:
            # Skip empty lines
            if not line:
                continue
            ioc_type, value, actor = line.strip().split(",")
            yield IoC(ioc_type, value, actor)


def process_iocs():
    """
    Process IoCs from a file and print counts for various metrics
    """
    grouped_ioc_types = defaultdict(list)
    grouped_ioc_values = defaultdict(list)
    grouped_ioc_actors = defaultdict(list)

    iocs = 0
    ioc_types = Counter()
    ioc_values = Counter()
    ioc_actors = Counter()

    for ioc in stream_iocs(ioc_file_name):
        # Group IoCs by type, value, and actor
        grouped_ioc_types[ioc.type].append([ioc.value, ioc.actor])
        grouped_ioc_values[ioc.value].append([ioc.type, ioc.actor])
        grouped_ioc_actors[ioc.actor].append([ioc.type, ioc.value])

        # Count IoCs by type, value, and actor
        iocs += 1
        ioc_types[ioc.type] += 1
        ioc_values[ioc.value] += 1
        ioc_actors[ioc.actor] += 1

    return {
        "groupings": {
            "types": grouped_ioc_types,
            "values": grouped_ioc_values,
            "actors": grouped_ioc_actors,
        },
        "counts": {
            "iocs": iocs,
            "types": len(ioc_types),
            "types_breakdown": ioc_types,
            "values": len(ioc_values),
            "values_breakdown": ioc_values,
            "actors": len(ioc_actors),
            "actors_breakdown": ioc_actors,
        },
    }


if __name__ == "__main__":
    results = process_iocs()

    print("##################################################")
    print("### General IoC Counts ###\n")
    print(f"Total IoCs: {results['counts']['iocs']}")
    print(f"Total IoC Types: {results['counts']['types']}")
    print(f"Total IoC Values: {results['counts']['values']}")
    print(f"Total IoC Actors: {results['counts']['actors']}")
    print("##################################################\n")

    types_keys = list(results["counts"]["types_breakdown"].keys())
    values_keys = list(results["counts"]["values_breakdown"].keys())
    actors_keys = list(results["counts"]["actors_breakdown"].keys())

    print("##################################################")
    print("### IoC Type Breakdown ###\n")
    for i in range(len(types_keys)):
        print(
            f"IoC Type ({types_keys[i]}): {results['counts']['types_breakdown'][types_keys[i]]}"
        )
    print("##################################################\n")

    print("##################################################")
    print("### IoC Value Breakdown ###\n")
    for i in range(len(values_keys)):
        print(
            f"IoC Value ({values_keys[i]}): {results['counts']['values_breakdown'][values_keys[i]]}"
        )
    print("##################################################\n")

    print("##################################################")
    print("### IoC Actor Breakdown ###\n")
    for i in range(len(actors_keys)):
        print(
            f"IoC Actor ({actors_keys[i]}): {results['counts']['actors_breakdown'][actors_keys[i]]}"
        )
    print("##################################################")
