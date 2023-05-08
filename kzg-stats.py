from pprint import pprint
import sys
# Execute sm_rank in CS:GO's console
# Player > Completed Maps
# Copy console output into a file
# python ./kzg-stats.py <file>

data = open(sys.argv[1]).readlines()
stats = { }
for datum in data:
    datum = datum.strip()
    if not datum:
        continue

    k, v = datum.split(' - ')
    l, r = v.split('Rank: ')[1].split('/')
    l, r = int(l), int(r)
    stats[k] = { 'percentile': round(((r - l) / r) * 100), 'rank': f'{l}/{r}' }
# Ordered dictionaries are a CPython implementation detail
stats = dict(sorted(stats.items(), key=lambda x: x[1]['percentile']))

print('{:<25} {:<10} {:<15}'.format('Map', 'Percentile', 'Rank'))
for k, v in stats.items():
    print('{:25} {:<10} {:<15}'.format(k, v['percentile'], v['rank']))
