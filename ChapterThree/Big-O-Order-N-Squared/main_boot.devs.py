
# O(nm)
def get_avg_brand_followers(all_handles, brand_name):
    count = 0  # count all handles containing the brand
    for handles in all_handles:
        for handle in handles:
            if brand_name in handle:
                count += 1  # increment the counter
    return count / len(all_handles)
