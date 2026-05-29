"""
Use the following version of the geometric progression
formula, in which
`a1` is the initial number of followers,
`r` is the multiplication constant, and
`n` is the number of months:
`total = a1 × r^n`
"""


def get_follower_prediction(follower_count, influencer_type, num_months):
    if influencer_type == "fitness":
        r = 4
    elif influencer_type == "cosmetic":
        r = 3
    else:
        r = 2
    
    return follower_count * (r ** num_months)
