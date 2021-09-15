if __name__ != '__main__':
    raise RuntimeError


import os


repodir = os.path.abspath(os.path.dirname(__file__))
productsdir = os.path.join(repodir, 'products')


publicrelease = sorted(set(
    os.path.splitext(filename)[0]
    for filename in os.listdir(productsdir)
    ))


def make_links(rootname, dname):
    return f'''\
[\
![{dname}.png]\
({rootname}/products/{dname}.png)\
]({rootname}/products/{dname}.png)

[Data]({rootname}/products/{dname}.csv)\
'''


links = '\n\n'.join(
    make_links(
        "https://rsbyrne.github.io/mobility-aus",
        dname,
        )
    for dname in publicrelease
    )

text = (
f'''
---
title: Welcome to the Australian Crisis Mobility Portal
---

This daily-updated portal aggregates mobility and case data \
from various sources to give a general picture \
of how Australians are responding to the ongoing COVID-19 crisis. \
It is a free and public resource \
meant for journalists, citizens, academics, \
and colleagues from across the COVID-19 volunteer analysis community. \
Feedback, queries, and requests may be directed to Rohan Byrne at <rohan.byrne@unimelb.edu.au>

NOTE: This portal was recently reconstructed. \
Links will be readded in the coming days \
and should be stable for the remainder of the COVID-19 crisis.

{links}
'''
)


with open('index.md', mode='w') as file:
    file.write(text)

