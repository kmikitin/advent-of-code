"""
--- Day 1: Sonar Sweep ---

As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle input) appears: each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.)
"""
# NOTE: pairwise is a thing in 3.10 itertools but I'm running 3.8
def pairwise(data_list):
    return [(x, y, z) for x, y, z in zip(data_list, data_list[1:], data_list[2:])]

def count_increased(tuples_list):
    total_increase = 0
    for a, b in tuples_list:
        if a < b:
            total_increase = total_increase + 1

    return total_increase

def get_number_of_increased_measurements(depths_file):

    with open(depths_file) as depths:
        depths_tuples = pairwise(depths.read().split())
        print(len(depths_tuples))
    
    return count_increased(depths_tuples)

# Off by 1?
answer = get_number_of_increased_measurements('sampled1.txt')
print(answer)


with open("d1puzzleinput.txt") as input:
    depths = [int(line.strip()) for line in input]
    print(len(depths))

depth_measurment_increases = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        depth_measurment_increases += 1

print(depth_measurment_increases)

"""
--- Part Two ---
Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the above example:

199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
"""