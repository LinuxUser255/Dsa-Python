"""
DSA Learning Module: Caching, Validation, and Normalization
============================================================

Real-World Application: LLM client for crypto analysis with
cached clients, probability validation, and edge filters.

KEY CONCEPTS:
- Memoization/Caching: Store computed results to avoid re-computation
- Input validation: Ensure data integrity with O(k) operations
- Normalization: Transform data to standard form
- argmax: Find key with maximum value in a dict
"""

from typing import Any, Dict, List, Optional


# =============================================================================
# CONCEPT 1: Simple Cache with Dictionary
# =============================================================================

# Global cache - this is a form of memoization
_client_cache: Dict[str, Any] = {}


PROVIDERS: Dict[str, Dict[str, str]] = {
    "grok": {
        "base_url": "https://api.x.ai/v1",
        "model": "grok-4-1-fast",
    },
    "openai": {
        "base_url": "https://api.openai.com/v1",
        "model": "gpt-4o",
    },
    "claude": {
        "base_url": "https://api.anthropic.com/v1",
        "model": "claude-3",
    },
}


def get_client(provider: str) -> Dict[str, str]:
    """
    Get cached client config. Only creates config once per provider.
    
    This is O(1) lookup for subsequent calls!
    
    Pattern: Check cache -> Return if exists -> Create if not -> Cache -> Return
    
    Real impact: Creating API clients is expensive (network handshakes).
    Caching means we only pay that cost once per provider.
    """
    if provider not in PROVIDERS:
        raise ValueError(f"Unknown provider: {provider}")
    
    if provider not in _client_cache:
        # Simulate expensive client creation
        print(f"    [Creating new client for '{provider}'...]")
        _client_cache[provider] = {
            "provider": provider,
            **PROVIDERS[provider],
            "initialized": True,
        }
    else:
        print(f"    [Using cached client for '{provider}']")
    
    return _client_cache[provider]


# =============================================================================
# CONCEPT 2: Probability Validation and Normalization
# =============================================================================

def validate_probabilities(probs: Dict[str, float]) -> Dict[str, float]:
    """
    Ensure probability distribution is valid.
    
    Requirements:
    1. All required keys exist (with defaults if missing)
    2. All values are floats (convert strings)
    3. Values sum to 1.0 (normalize if not)
    
    Time Complexity: O(k) where k = number of keys (constant, typically 4)
    
    This is essentially O(1) since k is fixed and small.
    """
    required_keys = ["up", "down", "sideways", "uncertain"]
    
    # Step 1: Ensure all keys exist - O(k)
    for key in required_keys:
        if key not in probs:
            probs[key] = 0.0
        # Convert strings to floats if needed
        if isinstance(probs[key], str):
            try:
                probs[key] = float(probs[key])
            except ValueError:
                probs[key] = 0.0
    
    # Step 2: Normalize to sum to 1.0 - O(k)
    total = sum(probs.values())
    
    if total > 0 and abs(total - 1.0) > 0.01:
        # Dict comprehension for normalization - O(k)
        probs = {k: v / total for k, v in probs.items()}
    
    return probs


# =============================================================================
# CONCEPT 3: argmax - Find Key with Maximum Value
# =============================================================================

def get_direction_bias(probs: Dict[str, float]) -> str:
    """
    Return the key with the highest probability (argmax).
    
    Example:
        {"up": 0.6, "down": 0.2, "sideways": 0.15, "uncertain": 0.05}
        Returns: "up"
    
    Time Complexity: O(k) - must check all values
    
    Python's max() with key parameter is the clean way to do this.
    """
    if not probs or all(v == 0 for v in probs.values()):
        return "uncertain"
    
    # max() with key=probs.get finds key whose value is maximum
    return max(probs, key=probs.get)


# =============================================================================
# CONCEPT 4: Threshold-Based Filtering with Hashmaps
# =============================================================================

# Horizon-specific thresholds stored in dict for O(1) lookup
CONFIDENCE_THRESHOLDS: Dict[str, float] = {
    "1h": 0.45,   # More aggressive for short-term
    "2h": 0.48,
    "4h": 0.52,
    "6h": 0.55,
    "12h": 0.60,
    "24h": 0.65,  # More conservative for daily
}


EDGE_THRESHOLDS: Dict[str, float] = {
    "1h": 0.42,
    "2h": 0.45,
    "4h": 0.50,
    "6h": 0.55,
    "12h": 0.62,
    "24h": 0.68,
}


def should_trade(
    direction: str,
    confidence: float,
    horizon: str,
    volume_ratio: float = 1.0,
) -> tuple:
    """
    Determine if we should act on a prediction using threshold filters.
    
    Multiple O(1) dict lookups combined into a decision.
    
    Returns: (should_trade: bool, reason: str)
    """
    # O(1) threshold lookups with defaults
    min_confidence = CONFIDENCE_THRESHOLDS.get(horizon, 0.50)
    min_edge = EDGE_THRESHOLDS.get(horizon, 0.50)
    
    # Volume threshold (varies by horizon)
    volume_thresholds = {
        "1h": 0.4, "2h": 0.45, "4h": 0.5,
        "6h": 0.6, "12h": 0.65, "24h": 0.7,
    }
    min_volume = volume_thresholds.get(horizon, 0.5)
    
    # Decision logic
    if direction in ["uncertain"]:
        return (False, "Direction is uncertain")
    
    if confidence < min_confidence:
        return (False, f"Confidence {confidence:.2f} < {min_confidence} threshold")
    
    if volume_ratio < min_volume:
        return (False, f"Volume {volume_ratio:.2f}x < {min_volume}x required")
    
    # Simple edge calculation
    edge = confidence * (1 + (volume_ratio - 1) * 0.1)
    if edge < min_edge:
        return (False, f"Edge {edge:.2f} < {min_edge} threshold")
    
    return (True, f"Edge {edge:.2f} passes all filters")


# =============================================================================
# CONCEPT 5: Provider Selection with Available Check
# =============================================================================

def get_available_providers(api_keys: Dict[str, str]) -> List[str]:
    """
    Filter providers to only those with configured API keys.
    
    Time Complexity: O(p) where p = number of providers (small constant)
    
    Uses dict membership check (O(1)) inside loop.
    """
    available = []
    for provider_name in PROVIDERS:
        # Check if API key exists and is non-empty
        if api_keys.get(provider_name):
            available.append(provider_name)
    
    return available


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1_memoize(func):
    """
    EXERCISE 1: Implement a memoization decorator.
    
    Create a decorator that caches function results.
    When called with same arguments, return cached result.
    
    Example usage:
        @exercise_1_memoize
        def expensive_calculation(n):
            return n ** 2
        
        expensive_calculation(5)  # Computes and caches
        expensive_calculation(5)  # Returns cached result
    
    Hint: Use a dict to store {args: result}
    """
    # YOUR CODE HERE
    pass


def exercise_2_normalize(values: List[float]) -> List[float]:
    """
    EXERCISE 2: Normalize a list of values to sum to 1.0.
    
    Given: [2, 3, 5]
    Return: [0.2, 0.3, 0.5]  # Each divided by sum (10)
    
    Handle edge case: if sum is 0, return equal distribution.
    """
    # YOUR CODE HERE
    pass


def exercise_3_argmax_argmin(values: Dict[str, float]) -> tuple:
    """
    EXERCISE 3: Find both the key with max value and key with min value.
    
    Given: {"a": 10, "b": 5, "c": 15, "d": 3}
    Return: ("c", "d")  # (argmax, argmin)
    
    Do this in a single pass through the dict (O(n)).
    """
    # YOUR CODE HERE
    pass


def exercise_4_filter_by_threshold(
    items: List[Dict[str, Any]],
    threshold_key: str,
    min_value: float,
) -> List[Dict[str, Any]]:
    """
    EXERCISE 4: Filter items where a specific key meets threshold.
    
    Given items like:
        [{"name": "A", "score": 0.8}, {"name": "B", "score": 0.3}]
    With threshold_key="score", min_value=0.5
    
    Return: [{"name": "A", "score": 0.8}]  # Only items with score >= 0.5
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# SOLUTIONS
# =============================================================================

def _solution_1_memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


def _solution_2(values):
    total = sum(values)
    if total == 0:
        return [1.0 / len(values)] * len(values) if values else []
    return [v / total for v in values]


def _solution_3(values):
    if not values:
        return (None, None)
    
    max_key = min_key = next(iter(values))
    max_val = min_val = values[max_key]
    
    for key, val in values.items():
        if val > max_val:
            max_val = val
            max_key = key
        if val < min_val:
            min_val = val
            min_key = key
    
    return (max_key, min_key)


def _solution_4(items, threshold_key, min_value):
    return [item for item in items if item.get(threshold_key, 0) >= min_value]


# =============================================================================
# DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("DSA Learning: Caching, Validation, Normalization")
    print("=" * 60)
    
    # Demo 1: Client caching
    print("\n1. Client Caching (Memoization):")
    client1 = get_client("grok")
    client2 = get_client("grok")  # Should use cache
    client3 = get_client("openai")
    print(f"   Same client? {client1 is client2}")
    
    # Demo 2: Probability validation
    print("\n2. Probability Validation & Normalization:")
    raw_probs = {"up": "0.5", "down": 0.3}  # Missing keys, string value
    print(f"   Raw: {raw_probs}")
    valid_probs = validate_probabilities(raw_probs.copy())
    print(f"   Valid: {valid_probs}")
    print(f"   Sum: {sum(valid_probs.values()):.2f}")
    
    # Demo 3: argmax
    print("\n3. argmax (Direction Bias):")
    probs = {"up": 0.6, "down": 0.2, "sideways": 0.15, "uncertain": 0.05}
    bias = get_direction_bias(probs)
    print(f"   Probs: {probs}")
    print(f"   Direction: {bias}")
    
    # Demo 4: Threshold filters
    print("\n4. Threshold-Based Filtering:")
    scenarios = [
        ("up", 0.70, "1h", 1.2),
        ("up", 0.40, "1h", 1.2),  # Low confidence
        ("down", 0.65, "24h", 0.5),  # Low volume
    ]
    for direction, conf, horizon, vol in scenarios:
        trade, reason = should_trade(direction, conf, horizon, vol)
        symbol = "✓" if trade else "✗"
        print(f"   {symbol} {direction}/{horizon}/conf={conf}/vol={vol}x: {reason}")
    
    # Demo 5: Available providers
    print("\n5. Filter Available Providers:")
    api_keys = {"grok": "key123", "openai": "", "claude": "key456"}
    available = get_available_providers(api_keys)
    print(f"   Configured keys: {list(api_keys.keys())}")
    print(f"   Available: {available}")
    
    print("\n" + "=" * 60)
    print("Try the exercises!")
    print("=" * 60)
