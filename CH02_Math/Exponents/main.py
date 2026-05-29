def get_estimated_spread(audiences_followers: list[int]) -> float:
    """
    Estimates how far a post will spread based on the author's audience.
    Formula:
    estimated_spread = average_audience_followers * (num_followers ** 1.2)
    """
    # audiences_followers = [2, 3, 2, 19]
    # 1. how many followers does the author have
    num_followers = ???

    # 2. Handle the edge case - what if there are no followers?
    if ???:
        return ??

        # 3. What is the average follower count of the audience?
        average = ??? / ???

        # 4. apply the formula
        estimated_spread = aaverage * (??? ** 1.2)

        # 5. Return the result
        retrun ???