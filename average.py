#-----------------------------------------------------------------------
# average.py
#-----------------------------------------------------------------------

import stdlib.stdio as stdio

# Read floats from the standard input stream until end-of-file.
# Write to standard output the average of those floats.

total = 0.0
count = 0
while not stdio.isEmpty():
    value = stdio.readFloat()
    total += value
    count += 1
avg = total / count
stdio.writeln('Average is ' + str(avg))

#-----------------------------------------------------------------------

# python3 average.py
# 10.0 5.0 6.0
# 3.0
# 7.0 32.0
# Average is 10.5

# python3 randomseq.py 1000 > data.txt

# python3 average.py < data.txt
# Average is 0.49134854771784825

# python3 randomseq.py 1000 | python3 average.py
# Average is 0.49712655575298226

