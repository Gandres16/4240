def max_teams(teamSizes, k):
    teamSizes.sort()  # Sort the team sizes in non-decreasing order
    maxTeams = 0  # Variable to store the maximum number of teams that can be formed

    for i in range(1, teamSizes[-1] + 1):
        reducedTeams = 0  # Number of teams that can be formed with team size i

        for size in teamSizes:
            if size > i:
                reducedTeams += min((size - i) // k, 1)  # Reduce team size of at most k teams

        maxTeams = max(maxTeams, reducedTeams)

    return maxTeams

    def maxIndex(steps, badIndex):
        maxIndex = 0  # Variable to store the maximum index that can be reached
        j = 1  # Starting value of j
        for i in range(steps):
            if maxIndex + j == badIndex:  # If the next index is the bad index, skip it
                j += 1
            maxIndex += j  # Move to the next index
            j += 1  # Increment j for the next step
        return maxIndex