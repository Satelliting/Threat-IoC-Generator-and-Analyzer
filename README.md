# Threat IoC Generator and Analyzer

Generate synthetic Indicators of Compromise (IPs, domains, URLs), compose randomized IoCs with actors, and analyze counts/breakdowns.

- No external dependencies (pure Python stdlib).
- Outputs text files with generated data and prints summary stats.

## Project Layout

- [generate_ips.py](generate_ips.py) — creates `threat_ips.txt`
- [generate_domains.py](generate_domains.py) — creates `threat_domains.txt`
- [generate_urls.py](generate_urls.py) — creates `threat_urls.txt`
- [generate_iocs.py](generate_iocs.py) — creates `threat_iocs.txt` (type,value,actor)
- [process_iocs.py](process_iocs.py) — reads `threat_iocs.txt` and prints counts/breakdowns
- Data files (generated): `threat_ips.txt`, `threat_domains.txt`, `threat_urls.txt`, `threat_iocs.txt`

## Quickstart

1. Optionally edit counts/toggles (see “Toggleable options”).
2. Generate base lists (only needed if using files; defaults are ON):
   - `python generate_ips.py`
   - `python generate_domains.py`
   - `python generate_urls.py`
3. Generate IoCs:
   - `python generate_iocs.py`
4. Analyze IoCs:
   - `python process_iocs.py`

On Windows you can use `python` or `py`, depending on your setup.

## Toggleable Options

- [generate_ips.py](generate_ips.py)

  - `desired_ip_count` — number of IPs to generate.
  - `output_file_name` — file to write IPs (default `threat_ips.txt`).

- [generate_domains.py](generate_domains.py)

  - `desired_domain_count` — number of domains to generate.
  - `output_file_name` — file to write domains (default `threat_domains.txt`).

- [generate_urls.py](generate_urls.py)

  - `desired_url_count` — number of URLs to generate.
  - `output_file_name` — file to write URLs (default `threat_urls.txt`).

- [generate_iocs.py](generate_iocs.py)

  - `desired_ioc_count` — number of IoCs to generate (default 500).
  - `ioc_file_name` — output CSV (default `threat_iocs.txt`).
  - `ioc_types` — list of types used, default `["ip","domain","url"]`.
  - `use_ip_file` / `use_domain_file` / `use_url_file` — when True, pick values from the corresponding `threat_*.txt` file; when False, generate random values inline.
  - `actors` — list of actor labels to assign randomly.

- [process_iocs.py](process_iocs.py)
  - No direct flags; it reads the `ioc_file_name` imported from [generate_iocs.py](generate_iocs.py) and prints:
    - Total IoCs, unique IoC types, unique values, unique actors
    - Breakdown counts by type, value, and actor

## Data Formats

- `threat_ips.txt`: one IPv4 per line.
- `threat_domains.txt`: one domain per line.
- `threat_urls.txt`: one URL per line.
- `threat_iocs.txt`: CSV with lines as `type,value,actor`. Values must not contain commas.

## Example Output (process_iocs.py)

##################################################

General IoC Counts
Total IoCs: 500
Total IoC Types: 3
Total IoC Values: 119
Total IoC Actors: 9
##################################################

IoC Type Breakdown
IoC Type (ip): 169
IoC Type (url): 169
IoC Type (domain): 162 ...
##################################################

IoC Value Breakdown
IoC Value (1.1.1.1): 169
IoC Value (example.com): 169
IoC Value (example.org): 162 ...
##################################################

IoC Actor Breakdown
IoC Actor (actor1): 169
IoC Actor (actor2): 169
IoC Actor (actor3): 162 ...
##################################################

## Important Notes

- Side effect on import: [process_iocs.py](process_iocs.py) imports from [generate_iocs.py](generate_iocs.py). Because [generate_iocs.py](generate_iocs.py) writes its output at module import time, running [process_iocs.py](process_iocs.py) will regenerate `threat_iocs.txt` using the current toggles in [generate_iocs.py](generate_iocs.py). If you want to analyze an existing `threat_iocs.txt` without regenerating it, move the file-writing block in [generate_iocs.py](generate_iocs.py) under `if __name__ == "__main__":` (or run [process_iocs.py](process_iocs.py) against a decoupled module).
- Duplicates are expected: IoC values are chosen with replacement (via `random.choice`), so counts may show repeated values.
- Reproducibility: Set a fixed RNG seed at the top of scripts (e.g., `random.seed(42)`) if you want deterministic outputs.
- Extending IoC types: Add a new type to `ioc_types`, provide a generator for its values (and optionally a supporting file + `use_*_file` toggle), and ensure the value format remains comma-free.

## Programmatic Use

You can import and reuse the analyzer:

```python
from process_iocs import process_iocs
results = process_iocs()  # returns dict with 'groupings' and 'counts'
```
