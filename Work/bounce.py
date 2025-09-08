# bounce.py
#
# Exercise 1.5

REBOUND_HEIGHT_FRACT = 3 / 5

curr_drop_height = 100  # in meters

for i in range(10):
    curr_drop_height *= REBOUND_HEIGHT_FRACT
    print(i + 1, round(curr_drop_height, 4))
