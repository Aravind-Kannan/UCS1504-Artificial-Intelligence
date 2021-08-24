# Initial State: (8, 0, 0)
# Goal State: 4 in any one jar
#     SAMPLE Goal State: (4, 1, 3)
# State: Total Water = 8L
# (8L jar, 5L jar, 3L jar)

# Action: Empty a jar or fill up another jar

jar_capacity = (8, 5, 3)


class Node():
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent


def gen_goal_test(cur_state):
    if 4 in cur_state.state:
        return True
    return False


def neighbours(cur_state):
    possible_states = []

    for i in range(len(cur_state.state)):
        # if source jar has water
        if cur_state.state[i] > 0:

            for j in range(len(cur_state.state)):

                # if destination jar differs from source jar
                if i != j:

                    # if destination jar is not completely full
                    if cur_state.state[j] < jar_capacity[j]:
                        possible_state = list(cur_state.state)
                        pourable = jar_capacity[j] - cur_state.state[j]

                        if cur_state.state[i] >= pourable:
                            # if source jar has more than the water pourable into destination,
                            # we fill destination jar
                            possible_state[i] -= pourable
                            possible_state[j] += pourable
                        else:
                            # if source jar has less than the water pourable into destination,
                            # we empty source jar
                            possible_state[i] -= cur_state.state[i]
                            possible_state[j] += cur_state.state[i]

                        possible_states.append(
                            Node(state=tuple(possible_state), parent=cur_state))

    return possible_states


def does_not_contain(frontier, neighbour):
    for node in frontier:
        if node.state == neighbour.state:
            return False
    return True
