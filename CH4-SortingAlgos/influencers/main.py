class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"

# dont touch above this line
def vanity(influencer):
    """
    Calculate the vanity score for a single influencer.
    Vanity score = (number of links in bio × 5) + number of selfies
    """
    # access the attributes of influencer object and calculate the vanity score
    selfies = influencer.num_selfies
    links = influencer.num_bio_links
    score = (links * 5) + selfies

    return score


def vanity_sort(influencers):
    """
    Return a new list of influencers sorted by increasing vanity score.
    Complexity: Time: O(n log n), Space: O(n)
    """
    sorted_influencers = sorted(influencers, key=vanity)

    return sorted_influencers
