# Bioart Creator

import random
import sys
import time

PAUSE = 0.15  # Try changing this value.

ROWS = [
    '         ##',    # Index 0 has no {}.
    '        #{0}-{1}#',
    '       #{0}---{1}#',
    '      #{0}-----{1}#',
    '     #{0}-------{1}#',
    '    #{0}---------{1}#',
    '   #{0}-----------{1}#',
    '#{0}-------------{1}#',
    '#{0}-----------{1}#',
    '##',              # Index 9 has no {}.
    '#{0}-----------{1}#',
    ' #{0}---------{1}#',
    '  #{0}-------{1}#',
    '   #{0}-----{1}#',
    '    #{0}---{1}#',
    '     #{0}-{1}#',
    '      #{0}---{1}#',
    '       #{0}-----{1}#']
# 123456789 <- Use this to measure the number of spaces

try:
    print('Press ctrl-c to exit')
    time.sleep(2)
    row_index = 0

    while True:  # Main program loop.
        # Increment row index to draw next row.
        row_index += 1
        if row_index == len(ROWS):
            row_index = 0

        # Row indexes  0 and 9 don't hhave nucleotides.
        if row_index == 0 or row_index == 9:
            print(ROWS[row_index])
            continue

        # Select random nucleotide pairs, guanine cytosine and adenine thymine.
        random_selection = random.randint(1, 4)
        if random_selection == 1:
            left_nucleotide, right_nucleotide = 'A', 'T'
        elif random_selection == 2:
            left_nucleotide, right_nucleotide = 'T', 'A'
        elif random_selection == 3:
            left_nucleotide, right_nucleotide = 'C', 'G'
        elif random_selection == 4:
            left_nucleotide, right_nucleotide = 'G', 'C'

        # Print row
        print(ROWS[row_index].format(left_nucleotide, right_nucleotide))
        time.sleep(PAUSE)

except KeyboardInterrupt:
    sys.exit()
