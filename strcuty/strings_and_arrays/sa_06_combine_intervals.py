# Combine Intervals
# Merge overlapping intervals

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, combine_intervals, that takes in a list of intervals as an argument. 
Each interval is a tuple containing a pair of numbers representing a start and end time. 
Your function should combine overlapping intervals and return a list containing the combined intervals.




EXAMPLES:
================================================================================
For example:

Given two intervals:

(1, 4) and (3, 7)

The intervals overlap and
should be combined into:

(1, 7)

You may return the combined intervals in any order.

You can assume that the input list contains at least one interval and all intervals are valid with start < end.

COMPLEXITY:
================================================================================

    n = number of intervals
    Time: O(nlogn)
    Space: O(n)


"""

# SOLUTION:
# ================================================================================

def combine_intervals(intervals):
  sorted_intervals = sorted(intervals, key=lambda x : x[0])
  combined = [ sorted_intervals[0] ]
  
  for current_interval in sorted_intervals[1:]:
    last_start, last_end = combined[-1]
    current_start, current_end = current_interval
    
    if current_start <= last_end:
      if current_end > last_end:
        combined[-1] = (last_start, current_end)
    else:
      combined.append(current_interval)
      
  return combined
  

