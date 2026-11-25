import Source.Process as Pro


def run(processes: list[Pro.Process],
        allocated: list[tuple[int, int, int]],
        maxRes: list[tuple[int, int, int]],
        available: list[int],): #-> tuple[list[Pro.Process], bool]:
    """
    This function runs the banker's algorithm on provided processes.
    Assumes three types of resources.

    :param processes: List of Processes involved
    :param allocated: Lists of allocated resources
    :param maxRes: Lists of maximum resources available to a process
    :param available: Lists of available resources
    :returns:
        (list) List of processes in the order they finished.
        (bool) Whether the algorithm finished or not.
    """

    finished = [False] * processes.__len__()
    need = [[m - a for m, a in zip(row_m, row_a)] for row_m, row_a in zip(maxRes, allocated)]

    return need, True


if __name__ == '__main__':
    print("steve")
    p1 = Pro.Process(1, 0, 0, 0)
    p2 = Pro.Process(2, 0, 0, 0)
    p3 = Pro.Process(3, 0, 0, 0)
    print(run([p1, p2, p3,],
              [(1, 2, 4), (2, 4, 2), (3, 1, 1),],
              [(4, 3, 6), (2, 4, 2), (3, 4, 3),],
              [5, 3, 4,])[0])