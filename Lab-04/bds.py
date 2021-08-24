from prob import jar_capacity, Node, neighbours

# Global variables
init_explored = set()
goal_explored = set()

# tru refactoring
init_parent = dict()
goal_parent = dict()


def is_adjancent(p, q):
    change = [p[i] - q[i] for i in range(3)]
    a = [(q[i] == jar_capacity[i] and change[i] != 0) for i in range(3)]
    b = [(q[i] == 0 and change[i] != 0) for i in range(3)]

    a1 = False
    b1 = False
    for i in range(3):
        a1 = a1 or a[i]
        b1 = b1 or b[i]

    return change[0]*change[1]*change[2] == 0 and (a1 or b1)


def parents(cur_state):
    possible_states = []

    for i in range(len(cur_state.state)):
        for j in range(len(cur_state.state)):

            possible_state = list(cur_state.state)

            # if destination jar differs from source jar
            if i != j:
                k = 0  # third jar
                for jar in range(len(cur_state.state)):
                    if(jar != i and jar != j):
                        k = jar

                if(possible_state[k] == 0 or possible_state[k] == jar_capacity):
                    while(possible_state[i] - 1 >= 0 and possible_state[j] + 1 <= jar_capacity[j]):
                        possible_state[i] -= 1
                        possible_state[j] += 1

                        # check if should, reverse
                        if(is_adjancent(possible_state, cur_state.state)):
                            possible_states.append(
                                Node(state=tuple(possible_state), parent=cur_state))

                else:
                    possible_state[j] = min(
                        cur_state.state[i] + cur_state.state[j], jar_capacity[j])
                    possible_state[i] -= possible_state[j] - cur_state.state[j]

                # check if should, reverse
                if(is_adjancent(possible_state, cur_state.state)):
                    possible_states.append(
                        Node(state=tuple(possible_state), parent=cur_state))

    return possible_states


def bds_search(initial_state, goal_state):
    init_explored.add(initial_state.state)
    init_queue = [initial_state]
    goal_explored.add(goal_state.state)
    goal_queue = [goal_state]

    while(len(init_queue) != 0 and len(goal_queue) != 0):

        # forward search
        ele = init_queue.pop(0)
        for neighbour in neighbours(ele):
            if neighbour.state not in init_explored:
                init_explored.add(neighbour.state)
                init_queue.append(neighbour)
                init_parent[neighbour.state] = ele.state

        # backward search
        ele = goal_queue.pop(0)
        for parent in parents(ele):
            if parent.state not in goal_explored:
                goal_explored.add(parent.state)
                goal_queue.append(parent)
                goal_parent[parent.state] = ele.state

        # check for intersection
        for state in init_explored:
            if state in goal_explored:
                return state

    return


def path_finder(initial_state, goal_state, m):
    path = []

    # backward towards intial state
    cur = tuple(m)
    while(cur != init_parent[initial_state]):
        path.append(cur)
        cur = init_parent[cur]
    path.reverse()

    # fowards towards goal state
    cur = tuple(m)

    while(cur != goal_parent[goal_state]):
        cur = goal_parent[cur]
        path.append(cur)

    return path[:-1]


def solver(initial_tuple, goal_tuple):
    initial_state = Node(state=initial_tuple, parent=None)
    goal_state = Node(state=goal_tuple, parent=None)

    init_parent[initial_tuple] = (0, 0, 0)
    goal_parent[goal_tuple] = (0, 0, 0)

    middle = bds_search(initial_state, goal_state)
    path = path_finder(initial_tuple, goal_tuple, middle)

    print("\nPath:\n")

    for i in path:
        print(i)

    print("\nCommon state: ", middle)

    print("\nStates------------------")
    print("\nFrom Initial State:")
    print("Number of states: ", len(init_explored))
    print(init_explored)
    print("\nFrom Goal State:")
    print("Number of states: ", len(goal_explored))
    print(goal_explored)


def main():
    # Sample test case:
    # Initial state: (8, 0, 0)
    print("-----BIDIRECTIONAL SEARCH-----")
    print("Maximum Jar capacity: ", jar_capacity)

    initial_state = (8, 0, 0)
    goal_state = (1, 4, 3)  # HARD CODED from Iterative Deepening

    print("Initial state: ", initial_state)
    print("Goal state: ", goal_state)

    solver(initial_state, goal_state)


if __name__ == "__main__":
    main()
