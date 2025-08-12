def recursive_solver(input_state, memo=None):
    # --- INIT ---
    if memo is None:
        memo = {}

    # --- MEMO CHECK ---
    if input_state in memo:
        return memo[input_state]

    # --- BASE CASE CHECKS ---
    if is_base_case(input_state):
        result = base_case_result(input_state)
        # Sanity check: base case should produce a valid result
        assert is_valid_result(result), f"Invalid base case result for {input_state}"
        memo[input_state] = result
        return result

    # --- PRE-LOOP INIT ---
    best = float('inf')
    made_progress = False  # track if we explored any valid subproblem

    # --- RECURSION ---
    for sub_state in generate_subproblems(input_state):
        assert problem_size(sub_state) < problem_size(input_state), \
            f"No progress from {input_state} → {sub_state}"

        candidate = recursive_solver(sub_state, memo)
        assert is_valid_result(candidate), f"Invalid subproblem result {candidate} for {sub_state}"

        made_progress = True
        best = min(best, transform_result(candidate, input_state))

    # --- POST-LOOP ASSERTS ---
    assert made_progress, f"No subproblems generated for {input_state}"
    assert best != float('inf'), f"No valid solution found for {input_state}"

    # --- RETURN ---
    memo[input_state] = best
    return best


from math import isqrt

def summing_squares(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]

    # Base case
    if n == 0:
        return 0

    best = float('inf')
    made_progress = False

    for base in range(1, isqrt(n) + 1):
        sq = base * base
        assert sq <= n, f"Square too large for n={n}"  # should never happen
        candidate = summing_squares(n - sq, memo)
        assert candidate != float('inf'), f"Bad subproblem result for n={n - sq}"
        made_progress = True
        best = min(best, 1 + candidate)

    assert made_progress, f"No update happened for n={n}"
    memo[n] = best
    return best

