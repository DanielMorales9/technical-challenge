
def backtracking(curr, customers, demands, results):
    """
    The recursive backtracking algorithm that incrementally
    construct the solution.
    :param curr: int
        The current customer index
    :param customers: int
        The number of customers (M)
    :param demands: list-like
        A list of M lists, one for each customer, consisting in
        a list of tuple (X, Y) where X determines the color index
        and Y indicates whether the customer likes X glossy or matte (0, 1)
    :param results: list
        The binary indicator vector that defines the solution

    :return: flag: bool
        Returns a boolean to indicate whether there is a solution
        to the given problem of not
    """
    if curr < customers:
        for c, m in demands[curr]:
            if results[c] == m or results[c] == -1:
                tmp = results[c]
                results[c] = m
                sol = backtracking(curr+1, customers, demands, results)
                if sol:
                    return sol
                else:
                    results[c] = tmp
        return False
    else:
        return True


def solver(problem):
    """
    The following method defines a backtracking algorithm to solve
    the paint batch optimization problem.
    It chooses the best available option from a given set of paint types
    that a customer likes and it then proceeds to the next customer.
    It backtracks if it finds conflicts between the customer tastes
    and the candidate partial solution.

    :param problem: dict
        A dictionary containing:
            "colors" the number of available colors (N)
            "customers" the number of customers (M)
            "demands" a list of M lists, one for each customer,
            each containing the paint types the customer likes.
    :return: result: string
        The result is a string representing a N binary indicator vector
        for the paint batch, where each ith digit represents ith color type:
        glossy or matte (respectively, 0 or 1).
        If a solution does not exists it returns the string 'IMPOSSIBLE'.

    """
    colors = problem.get("colors")
    customers = problem.get("customers")
    demands = problem.get("demands")
    results = [-1] * colors
    new_demands = []
    for c in range(customers):
        length = demands[c][0]
        d = demands[c][1:]
        demand = []
        for i in range(length):
            demand.append((d[2 * i] - 1, d[2 * i + 1]))
        demand = sorted(demand, key=lambda x: (length, x[1], x[0]))
        new_demands.append(demand)

    if backtracking(0, customers, new_demands, results):
        return " ".join(map(str, [0 if r == -1 else r for r in results]))
    else:
        return "IMPOSSIBLE"


def check(results, demands):
    all_customer_satisfied = True
    for customer_d in demands:
        at_least_one = False
        for c, m in customer_d:
            at_least_one = at_least_one or results[c] == m
        all_customer_satisfied = all_customer_satisfied and at_least_one
    return all_customer_satisfied


def add_one_to_binary(results):
    for i in reversed(range(len(results))):
        if results[i] == 0:
            results[i] = 1
            return results
        results[i] = 0
    return results


def solver_raw(problem):
    """
    The following method determines a brute force
    algorithm to solve the paint batch optimization problem.
    Basically, it enumerates and checks the satisfiability of
    all the possible solutions, starting from the cheapest batches.

    :param problem: dict
        A dictionary containing:
            "colors" the number of available colors (N)
            "customers" the number of customers (M)
            "demands" a list of M lists, one for each customer,
            each containing the paint types the customer likes.
    :return: result: string
        The result is a string representing a N binary indicator vector
        for the paint batch, where each ith digit represents ith color type:
        matte or glossy (respectively, 0 or 1).
        If a solution does not exists it returns the string 'IMPOSSIBLE'.

    """
    colors = problem.get("colors")
    customers = problem.get("customers")
    demands = problem.get("demands")

    new_demands = []
    for c in range(customers):
        length = demands[c][0]
        d = demands[c][1:]

        new_demands.append([(d[2 * i] - 1, d[2 * i + 1])
                            for i in range(length)])

    zeros = ([0] * colors)
    results = [0] * colors
    count = 0
    while count < 1:
        if check(results, new_demands):
            break
        results = add_one_to_binary(results)
        if results == zeros:
            count += 1
    if count == 1:
        return "IMPOSSIBLE"
    else:
        return " ".join(map(str, results))
