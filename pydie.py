import random
import time

total1 = int(0)
total2 = int(0)
total3 = int(0)
total4 = int(0)
total5 = int(0)
total6 = int(0)
runCount = 1

askedRun = input("How many rolls would you like to do? ")
if askedRun == str("benchmark"):
    t_end = time.time() + 5
    while time.time() < t_end:
        currentNumber = (random.randrange(1,7))
        if currentNumber == 1:
            total1 += 1
        elif currentNumber == 2:
            total2 += 1
        elif currentNumber == 3:
            total3 += 1
        elif currentNumber == 4:
            total4 += 1
        elif currentNumber == 5:
            total5 += 1
        elif currentNumber == 6:
            total6 += 1
        runCount = int(runCount) + int(1)
        print("Run: " + str(runCount) + ", rolled a " + str(currentNumber))
    print("Your average approximate roll rate is",runCount / 5,"rolls per second.")
    exit()
else:
    if int(askedRun) <int(1):
        print("Please input a number greater than one.")
        exit()

while runCount <int(askedRun) + 1:
    currentNumber = (random.randrange(1,7))
    if currentNumber == 1:
        total1 += 1
    elif currentNumber == 2:
        total2 += 1
    elif currentNumber == 3:
        total3 += 1
    elif currentNumber == 4:
        total4 += 1
    elif currentNumber == 5:
        total5 += 1
    elif currentNumber == 6:
        total6 += 1
    print("Run: " + str(runCount) + ", rolled a " + str(currentNumber))

    runCount = int(runCount) + int(1)
    
print("")
print(f"Total 1: {total1}")
print(f"Total 2: {total2}")
print(f"Total 3: {total3}")
print(f"Total 4: {total4}")
print(f"Total 5: {total5}")
print(f"Total 6: {total6}")
print("")

# Find the most commonly rolled number
totals = [total1, total2, total3, total4, total5, total6]
most_common_number = totals.index(max(totals)) + 1
print(f"Most commonly rolled number: {most_common_number}")

# Calculate the range (max - min) of roll counts
range_of_counts = max(totals) - min(totals)
print(f"Range of roll counts: {range_of_counts}")
print("")

# Calculate and print the percentage of the time each number was rolled
total_rolls = sum(totals)
percentages = [(count / total_rolls) * 100 for count in totals]
for i in range(6):
    print(f"Number {i+1} was rolled {totals[i]} times ({percentages[i]:.2f}% of the time).")
