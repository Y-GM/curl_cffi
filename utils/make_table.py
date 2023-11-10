import json

with open("utils/fingerprints.tsv", "w") as wf:
    wf.write("version\tja3n\takamai\n")
    for version in range(110, 120):
        with open(f"utils/fingerprints/ja3n-{version}.json") as rf:
            data = json.loads(rf.read())
        wf.write(f"{version}\t{data['ja3n_hash']}\t{data['akamai_hash']}\n")
