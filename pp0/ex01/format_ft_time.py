import time

current_time = time.time()

print("Seconds since January 1, 1970: {:,.4f} or {:.2e} in scientific notation".format(
    current_time,
    current_time
))

print(time.strftime("%b %d %Y"))