# Followers / Exponents
# The estimated_spread is calculated as follows:
# average_audience_followers * ( num_followers ^ 1.2 )
def get_estimated_spread(audiences_followers):
    num_followers = len(audiences_followers)
    if num_followers == 0:
        return 0

    sum = 0
    for num in audiences_followers:
        sum += num

    average_audience_followers = sum / num_followers
    return average_audience_followers * (num_followers**1.2)
