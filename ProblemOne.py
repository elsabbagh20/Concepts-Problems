def dailyStepsTracker(steps):
    
    steps = list(map(int, steps.split()))

    
    highestSteps = max(steps)
    lowestSteps = min(steps)

    averageSteps = sum(steps) / len(steps)

    sortedSteps = sorted(steps, reverse=True)

    print("Highest steps:", highestSteps)
    print("Lowest steps:", lowestSteps)
    print("Average steps:", averageSteps)
    print("Sorted steps (descending):", sortedSteps)

steps = input("Enter the number of steps taken each day in the month, separated by spaces: ")
dailyStepsTracker(steps)