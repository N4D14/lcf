#!/usr/bin/env python
with open('companiesdotest.txt', 'r') as fin, open('db_testing.txt', 'w') as fout:
    for line in fin:
        cols = str(line).split('\t')
        cols.pop(1)

        category = 2

        outline = str(category) + '\t'

        for col in cols:
            outline += col
            if outline.count('\n') == 0:
                outline += '\t'

        fout.write(outline)
