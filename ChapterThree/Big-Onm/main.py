# O(nm)

def get_avg_brand_followers(all_handles, brand_name):
    """
    calculate the average number of followers (per influencer)
    whose handles contain a given brand name.

    `all_handles`: contains a list of lists of strings
    (each inner list = one influencer's followers)

    `brand_name:` contains a string to search for in the handles

     THREE & FOUR: NESTED LOOP
     3. Loop over each influencer(outer loop) `n` times
        - For each inner list of handles
     4. Loop over each handle, of the current influencer
         (inner loop) `m` times
        - For each handle string:
            - Check if `brand_name` is in the handle
            - use 'in' keyword: `brand_name in handle`
            - If yes, increment `total_matching` by 1
     5. Calculate and return the average
        - If num_influencers == 0, return 0
        - else:
        return total_matching / num_influencers (as float)
    """

    # 2. Initialize Counters
    total_matching = 0 # count all handles containing the brand
    num_influencers = len(all_handles) # `n` length of all_handles

    for handles in all_handles: # loop over each influencer `n`
        for handle in handles: # handles of the current influencer `m
            try:
                if brand_name in handle:
                    total_matching += 1 # increment the counter
            except Exception as e:
                print(f'''An Error occurred
                 while matching brand names to handles: {e}''')
            else:
                # if no exception was raised, continue to next handle
                continue
    # 5. Calculate and return the average
    if num_influencers == 0:
        return 0
    else:
        return total_matching / num_influencers # as float










