#!/usr/bin/env python3
"""Compute weighted persona scores for Chapter 9. Criteria scored 1-10 by the author.
Run: python3 build/score.py  -> prints markdown tables."""
criteria = ["hardware","stability_rollback","ecosystem","polish","freshness","repos","maintenance","lifecycle","security","docs","governance","performance","host_flexibility"]
# Persona weights (sum not required to be 1; normalised)
personas = {
 "Combined (SWE+student+daily)": dict(hardware=5,stability_rollback=5,ecosystem=4,polish=4,freshness=3,repos=3,maintenance=3,lifecycle=3,security=2,docs=2,governance=2,performance=1,host_flexibility=3),
 "SWE (professional)":           dict(hardware=4,stability_rollback=5,ecosystem=4,polish=3,freshness=4,repos=3,maintenance=3,lifecycle=2,security=3,docs=2,governance=2,performance=1,host_flexibility=3),
 "CS student":                   dict(hardware=4,stability_rollback=5,ecosystem=5,polish=3,freshness=2,repos=2,maintenance=4,lifecycle=3,security=1,docs=3,governance=1,performance=1,host_flexibility=3),
 "Daily driver / newcomer":      dict(hardware=5,stability_rollback=4,ecosystem=3,polish=5,freshness=2,repos=2,maintenance=5,lifecycle=4,security=2,docs=3,governance=1,performance=1,host_flexibility=1),
 "Tinkerer / enthusiast":        dict(hardware=3,stability_rollback=2,ecosystem=2,polish=2,freshness=5,repos=5,maintenance=1,lifecycle=1,security=2,docs=4,governance=2,performance=3,host_flexibility=5),
}
# Scores: hardware, stability_rollback, ecosystem, polish, freshness, repos, maintenance(10=none), lifecycle, security, docs, governance, performance, host_flexibility(10=fully mutable FHS host)
D = {
 "Fedora Workstation / KDE": [9,8,8,9,8,7,8,6,9,8,8,7,10],
 "Ubuntu 26.04 LTS / Kubuntu":[9,8,10,8,6,7,9,10,8,8,7,7,10],
 "Linux Mint 22.x":          [8,8,9,8,4,7,9,9,7,8,6,7,10],
 "Pop!_OS 24.04":            [9,7,8,7,7,7,8,6,6,6,5,7,10],
 "Debian 13 stable":         [6,9,8,6,3,8,9,9,8,7,9,7,10],
 "Arch Linux":               [9,6,7,6,10,10,4,7,6,10,8,8,10],
 "EndeavourOS":              [9,6,7,7,10,10,5,7,6,9,7,8,10],
 "CachyOS":                  [9,7,7,8,10,10,5,7,6,7,6,9,10],
 "Manjaro":                  [8,5,6,7,8,7,5,7,6,6,4,7,10],
 "openSUSE Tumbleweed":      [9,9,6,8,9,7,7,7,9,7,7,7,10],
 "openSUSE Slowroll":        [8,9,6,8,7,7,8,7,9,6,6,7,10],
 "Bluefin / Aurora":         [9,10,7,9,8,6,10,7,9,7,6,7,5],
 "Bluefin DX / Aurora DX":   [9,10,7,9,8,7,10,7,9,7,6,7,6],
 "Bazzite":                  [10,10,7,9,8,6,10,7,8,7,6,8,5],
 "Fedora Silverblue/Kinoite":[8,10,6,8,8,5,9,6,9,6,8,7,5],
 "openSUSE Aeon":            [7,10,5,8,9,5,10,7,10,5,6,7,4],
 "NixOS":                    [8,10,5,7,10,10,4,8,7,6,6,7,6],
 "Void Linux":               [7,6,4,6,9,6,5,7,6,7,5,8,10],
 "Gentoo":                   [8,6,4,5,10,9,2,7,7,9,7,8,10],
 "Zorin OS 18":              [8,8,8,8,3,7,9,8,7,6,5,7,10],
}
def score(vals, w):
    tot = sum(w[c] for c in criteria)
    return sum(v*w[c] for v,c in zip(vals,criteria))/tot
print("## Per-persona weighted scores (0–10)\n")
hdr = "| Distro | " + " | ".join(personas) + " |"
print(hdr); print("|---|" + "---|"*len(personas))
rows=[]
for d,v in D.items():
    s=[score(v,w) for w in personas.values()]
    rows.append((d,s))
rows.sort(key=lambda r:-r[1][0])
for d,s in rows:
    print(f"| {d} | " + " | ".join(f"{x:.1f}" for x in s) + " |")
print("\n## Rank per persona\n")
for i,p in enumerate(personas):
    order = sorted(rows,key=lambda r:-r[1][i])[:6]
    print(f"**{p}:** " + ", ".join(f"{d} ({s[i]:.1f})" for d,s in order) + "\n")
