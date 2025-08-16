def job_scheduling(jobs):
    """
    4. Job Scheduling (Weighted / Deadlines)
    Simple case: maximize jobs before deadlines.
    Greedy → sort by deadline, fill slots backwards.
    """
    jobs.sort(key=lambda x: x[1])  # (profit, deadline)
    n = len(jobs)
    slots = [False] * n
    total_profit = 0

    for profit, deadline in reversed(jobs):
        for d in range(min(n, deadline)-1, -1, -1):
            if not slots[d]:
                slots[d] = True
                total_profit += profit
                break
    return total_profit

"""
✅ Used in CPU task scheduling, maximizing profit.
"""