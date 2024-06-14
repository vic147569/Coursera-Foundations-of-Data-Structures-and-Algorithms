from pulp import *


def check_status(status):
    if status == constants.LpStatusInfeasible:
        print("Problem is infeasible")
        return
    elif status == constants.LpStatusUnbounded:
        print("Problem is unbounded. Cannot proceed")
        return
    else:
        assert (
            status == constants.LpStatusOptimal
        ), "Something went wrong while solving since status is either undefined or unsolved"

        print("Success: optimal answer found")
        return


def solve_assignment1():
    lpModel = LpProblem("Assignment", LpMaximize)

    # dec var
    x = [LpVariable(f"x{i}", -15, 15) for i in range(6)]

    # objective
    lpModel += 2 * x[0] - 3 * x[1] + 1 * x[2]

    # constraint
    lpModel += x[0] - x[1] + x[2] <= 5
    lpModel += x[0] - x[1] + 4 * x[2] <= 7
    lpModel += x[0] + 2 * x[1] - x[2] + x[3] <= 14
    lpModel += x[2] - x[3] + x[4] <= 7

    status = lpModel.solve()

    if status == constants.LpStatusInfeasible:
        print("Problem is infeasible")
        return
    elif status == constants.LpStatusUnbounded:
        print("Problem is unbounded. Cannot proceed")
        return
    else:
        assert (
            status == constants.LpStatusOptimal
        ), "Something went wrong while solving since status is either undefined or unsolved"

        print("Success: optimal answer found")
        return


def solve_assignment2():
    lpModel = LpProblem("Assignment2", LpMinimize)

    # dec var
    x = [LpVariable(f"x{i}", -1, 1) for i in range(3)]

    # objective function
    lpModel += 2 * x[0] - 3 * x[1] + 1 * x[2]

    # constraint
    lpModel += x[0] - x[1] >= 0.5
    lpModel += x[0] - x[1] <= 0.75
    lpModel += x[1] - x[2] <= 1.25
    lpModel += x[1] - x[2] >= 0.95

    status = lpModel.solve()

    check_status(status)


# solve_assignment1()
solve_assignment2()
