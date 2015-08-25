#!/usr/bin/env python
with open('companiesdonttest.txt', 'r') as fin, open('db_nontesting.txt', 'w') as fout:
    for line in fin:
        cols = str(line).split('\t')

        category = 1
        if cols[0] == 'V':
            category = 3
        elif cols[0] == 'L':
            category = 4
        elif cols[0] == 'M':
            category = 5
        elif cols[0] == 'V L':
            category = 6
        elif cols[0] == 'V M':
            category = 7

        outline = str(category) + '\t'
        cols.pop(0)

        for col in cols:
            outline += col
            if outline.count('\n') == 0:
                outline += '\t'

        fout.write(outline)
