"""
DSA Learning Module: Hashmaps (Dictionaries) - O(1) Lookups
============================================================

Real-World Application: Time horizon mapping and provider routing
from a cryptocurrency prediction system.

KEY CONCEPTS:
- Python dicts are hashmaps with O(1) average lookup/insert/delete
- Hash collisions can degrade to O(n), but Python handles this well
- Hashmaps are ideal for: config lookup, caching, counting, grouping
"""

from datetime import timedelta
from typing import Any, Dict, Optional


# =============================================================================
# CONCEPT 1: Configuration Hashmaps - O(1) Lookup
# =============================================================================

# Instead of if-elif chains (O(n) worst case), use a dict (O(1))
HORIZON_DELTAS: Dict[str, timedelta] = {
    "1h": timedelta(hours=1),
    "2h": timedelta(hours=2),
    "4h": timedelta(hours=4),
    "6h": timedelta(hours=6),
    "12h": timedelta(hours=12),
    "24h": timedelta(hours=24),
}


def get_horizon_delta(horizon: str) -> timedelta:
    """
    O(1) lookup with default fallback.
    
    Using dict.get() is both safe AND fast:
    - No KeyError if key missing
    - Still O(1) time complexity
    
    BAD ALTERNATIVE (O(n) linear scan):
        if horizon == "1h": return timedelta(hours=1)
        elif horizon == "2h": return timedelta(hours=2)
        ...
    """
    return HORIZON_DELTAS.get(horizon, timedelta(hours=1))


# =============================================================================
# CONCEPT 2: Provider Routing - O(1) Directory Selection
# =============================================================================

PROVIDER_DIRS: Dict[str, str] = {
    "grok": "data/queries",
    "claude": "data/queries_claude",
    "openai": "data/queries_openai",
}


def get_provider_path(provider: str) -> str:
    """
    O(1) routing instead of if-elif chains.
    
    Real impact: When processing 10,000 predictions, this runs
    10,000 times. O(1) vs O(n) matters at scale!
    """
    return PROVIDER_DIRS.get(provider, PROVIDER_DIRS["grok"])


# =============================================================================
# CONCEPT 3: Membership Testing - O(1) with Sets/Dicts
# =============================================================================

# Use sets for membership tests (O(1)) instead of lists (O(n))
VALID_HORIZONS = {"1h", "2h", "4h", "6h", "12h", "24h"}  # Set = O(1)
# VALID_HORIZONS_LIST = ["1h", "2h", "4h", "6h", "12h", "24h"]  # List = O(n)


def is_valid_horizon(horizon: str) -> bool:
    """
    O(1) membership test with set.
    
    With list: "24h" in VALID_HORIZONS_LIST  # O(n) - scans all elements
    With set:  "24h" in VALID_HORIZONS       # O(1) - hash lookup
    """
    return horizon in VALID_HORIZONS


# =============================================================================
# CONCEPT 4: Building Records with Dict Unpacking
# =============================================================================

def enrich_payload(payload: Dict[str, Any], metadata: Dict[str, Any]) -> Dict[str, Any]:
    """
    O(n+m) where n,m are dict sizes - still efficient.
    
    Dict unpacking (**) creates new dict without modifying originals.
    This is the Pythonic way to merge dicts.
    """
    return {
        **payload,          # Unpack original payload
        **metadata,         # Add metadata (overwrites if keys collide)
        "enriched": True,   # Add new fields
    }


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1_status_codes() -> Dict[int, str]:
    """
    EXERCISE 1: Create a hashmap for HTTP status codes.
    
    Map these status codes to their descriptions:
    - 200 -> "OK"
    - 201 -> "Created"
    - 400 -> "Bad Request"
    - 404 -> "Not Found"
    - 500 -> "Internal Server Error"
    
    Return the dict.
    """
    # YOUR CODE HERE
    pass


def exercise_2_safe_lookup(status_codes: Dict[int, str], code: int) -> str:
    """
    EXERCISE 2: Implement safe O(1) lookup.
    
    Return the status description for the given code.
    If code doesn't exist, return "Unknown Status".
    
    Hint: Use dict.get() with a default value.
    """
    # YOUR CODE HERE
    pass


def exercise_3_frequency_counter(items: list) -> Dict[Any, int]:
    """
    EXERCISE 3: Count item frequencies using a hashmap.
    
    Given: ["apple", "banana", "apple", "cherry", "banana", "apple"]
    Return: {"apple": 3, "banana": 2, "cherry": 1}
    
    This is O(n) - one pass through the list!
    
    Hint: Use dict.get(key, default) to handle missing keys.
    """
    # YOUR CODE HERE
    pass


def exercise_4_two_sum(nums: list, target: int) -> tuple:
    """
    EXERCISE 4: Classic Two Sum problem using hashmap.
    
    Find two numbers that add up to target, return their indices.
    
    Example:
        nums = [2, 7, 11, 15], target = 9
        Return: (0, 1)  # because nums[0] + nums[1] = 2 + 7 = 9
    
    NAIVE: O(n²) - check every pair with nested loops
    OPTIMAL: O(n) - use hashmap to store complements
    
    Strategy:
    1. For each number, calculate complement = target - number
    2. Check if complement exists in hashmap (O(1) lookup!)
    3. If yes, return indices. If no, store number -> index.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# SOLUTIONS (Don't peek until you try!)
# =============================================================================

def _solution_1():
    return {
        200: "OK",
        201: "Created",
        400: "Bad Request",
        404: "Not Found",
        500: "Internal Server Error",
    }


def _solution_2(status_codes, code):
    return status_codes.get(code, "Unknown Status")


def _solution_3(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def _solution_4(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:  # O(1) lookup!
            return (seen[complement], i)
        seen[num] = i
    return None


# =============================================================================
# DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("DSA Learning: Hashmaps (O(1) Lookups)")
    print("=" * 60)
    
    # Demo 1: Horizon lookup
    print("\n1. O(1) Config Lookup:")
    for h in ["1h", "6h", "24h", "invalid"]:
        delta = get_horizon_delta(h)
        print(f"   '{h}' -> {delta}")
    
    # Demo 2: Membership test
    print("\n2. O(1) Membership Test:")
    test_horizons = ["1h", "3h", "6h", "1w"]
    for h in test_horizons:
        valid = is_valid_horizon(h)
        print(f"   '{h}' valid? {valid}")
    
    # Demo 3: Dict merging
    print("\n3. Dict Unpacking (Merging):")
    original = {"pair": "BTC/USD", "price": 95000}
    meta = {"timestamp": "2025-02-09T17:00:00Z", "source": "kraken"}
    merged = enrich_payload(original, meta)
    print(f"   Original: {original}")
    print(f"   Merged:   {merged}")
    
    # Demo 4: Two Sum with hashmap
    print("\n4. Two Sum O(n) Solution:")
    nums = [2, 7, 11, 15]
    target = 9
    result = _solution_4(nums, target)
    print(f"   nums={nums}, target={target}")
    print(f"   Indices: {result}")
    
    print("\n" + "=" * 60)
    print("Try the exercises above! Run: python 01_hashmaps_db.py")
    print("=" * 60)
