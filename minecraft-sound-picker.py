import datetime
import os
import random
import time


def get_random_file(path):
    """
    All categories will have the same chance to be picked
    """
    listdir = os.listdir(path)
    file = random.choice(listdir)
    if os.path.isdir(os.path.join(path, file)):
        return get_random_file(os.path.join(path, file))
    else:
        return os.path.join(path, file)


filename = get_random_file("sounds")
cmd = "mpv {} --no-terminal".format(filename)

print(f'[{datetime.datetime.now():%Y-%m-%d %H:%M}] Playing: {filename}')

# Set (minimum) seconds of playback time (optional)
loop_seconds = None

if loop_seconds:
    start_time = time.time()
    end_time = start_time
    while end_time - start_time < loop_seconds:
        os.system(cmd)
        end_time = time.time()
else:
    os.system(cmd)
