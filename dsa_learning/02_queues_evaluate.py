"""
DSA Learning Module: Queues and Batch Processing
=================================================

Real-World Application: Evaluating pending cryptocurrency predictions
using FIFO (First-In-First-Out) queue patterns.

KEY CONCEPTS:
- Queue: FIFO data structure - first item added is first processed
- Time-based task queues: items become "ready" when time condition met
- Batch processing: O(n) iteration with O(1) operations inside
- Grouping with nested dicts: organizing data efficiently
"""

from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


# =============================================================================
# CONCEPT 1: Time-Based Task Queue
# =============================================================================

@dataclass
class Task:
    """A task that becomes ready at a specific time."""
    id: str
    target_time: datetime
    data: Dict[str, Any]
    processed: bool = False


class TimeBasedQueue:
    """
    A queue where tasks become eligible only after their target_time.
    
    Real-world use: Predictions made at time T need to be evaluated
    at time T + horizon (e.g., 1 hour later).
    
    Time Complexity:
    - add_task(): O(1) - append to list
    - get_pending(): O(n) - scan all tasks, but O(1) checks inside
    - process_task(): O(1) - update flag
    """
    
    def __init__(self):
        self._tasks: List[Task] = []
    
    def add_task(self, task_id: str, target_time: datetime, data: Dict[str, Any]) -> None:
        """Add a new task. O(1) operation."""
        self._tasks.append(Task(id=task_id, target_time=target_time, data=data))
    
    def get_pending(self) -> List[Task]:
        """
        Find all tasks that are ready to process.
        
        A task is pending if:
        1. target_time has passed (target_time <= now)
        2. Not already processed
        
        This is O(n) iteration but each check is O(1).
        """
        now = datetime.now(timezone.utc)
        pending = []
        
        for task in self._tasks:
            # O(1) checks: boolean flag and datetime comparison
            if not task.processed and task.target_time <= now:
                pending.append(task)
        
        return pending
    
    def mark_processed(self, task_id: str) -> bool:
        """Mark a task as processed. O(n) to find, O(1) to update."""
        for task in self._tasks:
            if task.id == task_id:
                task.processed = True
                return True
        return False


# =============================================================================
# CONCEPT 2: FIFO Queue with collections.deque
# =============================================================================

def demonstrate_deque():
    """
    collections.deque is optimized for FIFO operations.
    
    List vs Deque for queue operations:
    - list.append(): O(1) amortized
    - list.pop(0):   O(n) - must shift all elements!
    
    - deque.append():    O(1)
    - deque.popleft():   O(1) - optimized for both ends!
    
    Use deque when you need frequent insertions/removals at both ends.
    """
    # Simulate processing predictions in order
    prediction_queue = deque()
    
    # Add predictions (O(1) each)
    prediction_queue.append({"id": "pred_001", "pair": "BTC/USD"})
    prediction_queue.append({"id": "pred_002", "pair": "ETH/USD"})
    prediction_queue.append({"id": "pred_003", "pair": "XMR/USD"})
    
    # Process in FIFO order (O(1) each)
    results = []
    while prediction_queue:
        pred = prediction_queue.popleft()  # O(1) - the key advantage!
        results.append(f"Processed {pred['id']}")
    
    return results


# =============================================================================
# CONCEPT 3: Grouping Data with Nested Dicts
# =============================================================================

def group_by_category(items: List[Dict[str, Any]], key: str) -> Dict[str, List[Dict]]:
    """
    Group items by a category key using nested dictionaries.
    
    Example from evaluate.py:
    Group predictions by horizon and pair:
        by_horizon_pair["1h"]["BTC_USD"] = [file1, file2, ...]
    
    Time Complexity: O(n) - single pass through items
    - dict.setdefault(): O(1) average
    - list.append(): O(1) amortized
    """
    grouped: Dict[str, List[Dict]] = {}
    
    for item in items:
        category = item.get(key, "unknown")
        # setdefault: get value if exists, else set default and return it
        # This is O(1) and cleaner than checking `if category not in grouped`
        grouped.setdefault(category, []).append(item)
    
    return grouped


def group_by_two_levels(
    items: List[Dict[str, Any]], 
    key1: str, 
    key2: str
) -> Dict[str, Dict[str, List[Dict]]]:
    """
    Two-level grouping: items grouped by key1, then by key2.
    
    Real example: Group predictions by horizon, then by trading pair.
    
    Structure:
        {
            "1h": {
                "BTC_USD": [pred1, pred2],
                "ETH_USD": [pred3]
            },
            "6h": {
                "BTC_USD": [pred4]
            }
        }
    
    Time Complexity: O(n) - still single pass!
    """
    grouped: Dict[str, Dict[str, List[Dict]]] = {}
    
    for item in items:
        level1 = item.get(key1, "unknown")
        level2 = item.get(key2, "unknown")
        
        # Two levels of setdefault - still O(1) each
        grouped.setdefault(level1, {}).setdefault(level2, []).append(item)
    
    return grouped


# =============================================================================
# CONCEPT 4: Batch Processing with Statistics
# =============================================================================

def batch_evaluate(predictions: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Process predictions and compute statistics in a single O(n) pass.
    
    Real-world: Count correct/incorrect predictions for accuracy report.
    
    Strategy: Use counters (integers) instead of storing all results.
    - Memory: O(1) for counters vs O(n) for storing results
    - Time: O(n) - single pass
    """
    stats = {
        "total": 0,
        "correct": 0,
        "incorrect": 0,
        "skipped": 0,
    }
    
    for pred in predictions:
        stats["total"] += 1
        
        # Simulate evaluation logic
        outcome = pred.get("outcome")
        if outcome == "correct":
            stats["correct"] += 1
        elif outcome == "incorrect":
            stats["incorrect"] += 1
        else:
            stats["skipped"] += 1
    
    # Compute derived statistics
    scored = stats["correct"] + stats["incorrect"]
    stats["accuracy_pct"] = (stats["correct"] / scored * 100) if scored > 0 else 0.0
    
    return stats


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1_implement_queue():
    """
    EXERCISE 1: Implement a simple FIFO queue using deque.
    
    Create a class SimpleQueue with methods:
    - enqueue(item): Add item to back of queue
    - dequeue(): Remove and return item from front (raise if empty)
    - peek(): Return front item without removing (raise if empty)
    - is_empty(): Return True if queue is empty
    - size(): Return number of items
    
    All operations should be O(1)!
    """
    # YOUR CODE HERE
    pass


def exercise_2_process_in_order(tasks: List[Dict]) -> List[str]:
    """
    EXERCISE 2: Process tasks in FIFO order using deque.
    
    Given a list of tasks like:
        [{"id": "t1", "action": "send"}, {"id": "t2", "action": "save"}]
    
    Return a list of strings:
        ["Processed t1: send", "Processed t2: save"]
    
    Use deque for O(1) popleft operations.
    """
    # YOUR CODE HERE
    pass


def exercise_3_group_transactions(transactions: List[Dict]) -> Dict[str, List[Dict]]:
    """
    EXERCISE 3: Group transactions by type.
    
    Given transactions like:
        [
            {"id": 1, "type": "buy", "amount": 100},
            {"id": 2, "type": "sell", "amount": 50},
            {"id": 3, "type": "buy", "amount": 200},
        ]
    
    Return grouped by type:
        {
            "buy": [{"id": 1, ...}, {"id": 3, ...}],
            "sell": [{"id": 2, ...}]
        }
    """
    # YOUR CODE HERE
    pass


def exercise_4_calculate_stats(numbers: List[int]) -> Dict[str, float]:
    """
    EXERCISE 4: Calculate statistics in a single O(n) pass.
    
    Return a dict with:
    - count: total numbers
    - sum: sum of all numbers
    - mean: average
    - min: minimum value
    - max: maximum value
    
    Challenge: Do this in ONE loop (O(n)), not multiple passes.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# SOLUTIONS
# =============================================================================

class _SolutionSimpleQueue:
    """Solution for Exercise 1"""
    def __init__(self):
        self._data = deque()
    
    def enqueue(self, item):
        self._data.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data.popleft()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data[0]
    
    def is_empty(self):
        return len(self._data) == 0
    
    def size(self):
        return len(self._data)


def _solution_2(tasks):
    q = deque(tasks)
    results = []
    while q:
        task = q.popleft()
        results.append(f"Processed {task['id']}: {task['action']}")
    return results


def _solution_3(transactions):
    grouped = {}
    for t in transactions:
        grouped.setdefault(t["type"], []).append(t)
    return grouped


def _solution_4(numbers):
    if not numbers:
        return {"count": 0, "sum": 0, "mean": 0, "min": 0, "max": 0}
    
    count = 0
    total = 0
    min_val = float('inf')
    max_val = float('-inf')
    
    for num in numbers:  # Single O(n) pass
        count += 1
        total += num
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    return {
        "count": count,
        "sum": total,
        "mean": total / count,
        "min": min_val,
        "max": max_val,
    }


# =============================================================================
# DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("DSA Learning: Queues and Batch Processing")
    print("=" * 60)
    
    # Demo 1: Time-based queue
    print("\n1. Time-Based Task Queue:")
    queue = TimeBasedQueue()
    now = datetime.now(timezone.utc)
    
    # Add tasks with different target times
    from datetime import timedelta
    queue.add_task("pred_1", now - timedelta(hours=1), {"pair": "BTC/USD"})  # Ready
    queue.add_task("pred_2", now + timedelta(hours=1), {"pair": "ETH/USD"})  # Not ready
    queue.add_task("pred_3", now - timedelta(minutes=30), {"pair": "XMR/USD"})  # Ready
    
    pending = queue.get_pending()
    print(f"   Total tasks: 3")
    print(f"   Pending now: {len(pending)}")
    for task in pending:
        print(f"      - {task.id}: {task.data['pair']}")
    
    # Demo 2: deque vs list
    print("\n2. deque FIFO Operations:")
    results = demonstrate_deque()
    for r in results:
        print(f"   {r}")
    
    # Demo 3: Grouping
    print("\n3. Two-Level Grouping:")
    predictions = [
        {"horizon": "1h", "pair": "BTC_USD", "id": "p1"},
        {"horizon": "1h", "pair": "BTC_USD", "id": "p2"},
        {"horizon": "1h", "pair": "ETH_USD", "id": "p3"},
        {"horizon": "6h", "pair": "BTC_USD", "id": "p4"},
    ]
    grouped = group_by_two_levels(predictions, "horizon", "pair")
    for horizon, pairs in grouped.items():
        print(f"   [{horizon}]")
        for pair, items in pairs.items():
            print(f"      {pair}: {len(items)} predictions")
    
    # Demo 4: Batch statistics
    print("\n4. Batch Statistics (Single O(n) Pass):")
    preds = [
        {"outcome": "correct"},
        {"outcome": "correct"},
        {"outcome": "incorrect"},
        {"outcome": "correct"},
        {"outcome": "skipped"},
    ]
    stats = batch_evaluate(preds)
    print(f"   Total: {stats['total']}")
    print(f"   Correct: {stats['correct']}")
    print(f"   Accuracy: {stats['accuracy_pct']:.1f}%")
    
    print("\n" + "=" * 60)
    print("Try the exercises! Solutions are at the bottom.")
    print("=" * 60)
