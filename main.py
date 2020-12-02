# TU20
lastnum = 0
with open("counter.txt", "r") as wholefile:
    for line in wholefile:
        lastnum = lastnum + 1
with open("counter.txt", "a") as existing_file:
    for i in range(1, 11):
        line_to_write = "\n" + str(i + lastnum)
        existing_file.write(line_to_write)
