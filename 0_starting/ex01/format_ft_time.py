import time

print(
    "Seconds since January 1, 1970:",
    time.time(),
    "or",
    "{:e}".format(time.time()),
    "in scientific notation.",
)
print(time.strftime("%b %d %Y"))
