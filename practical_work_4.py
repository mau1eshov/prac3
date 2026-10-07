"""Практикалық жұмыс 4: Minimax, альфа-бета, Eval, Expectimax."""

TREE = {
    "A": ["B", "C"],
    "B": ["D", "E"], "C": ["F", "G"],
    "D": ["H", "I"], "E": ["J", "K"],
    "F": ["L", "M"], "G": ["N", "O"],
}
VALUES = {"H": 4, "I": 9, "J": 7, "K": 2,
          "L": 3, "M": 8, "N": 6, "O": 1}


def is_terminal(state):
    return state in VALUES


def successors(state, reverse=False):
    children = TREE.get(state, [])
    return list(reversed(children)) if reverse else children[:]


def utility(state):
    return VALUES[state]


def minimax(state, maximizing, counter, reverse=False):
    counter[0] += 1
    if is_terminal(state):
        return utility(state)
    value = float("-inf") if maximizing else float("inf")
    for child in successors(state, reverse):
        result = minimax(child, not maximizing, counter, reverse)
        value = max(value, result) if maximizing else min(value, result)
    return value


def alphabeta(state, alpha, beta, maximizing, counter,
              reverse=False, visited=None):
    counter[0] += 1
    if visited is not None:
        visited.append(state)
    if is_terminal(state):
        return utility(state)
    value = float("-inf") if maximizing else float("inf")
    for child in successors(state, reverse):
        result = alphabeta(child, alpha, beta, not maximizing,
                           counter, reverse, visited)
        if maximizing:
            value = max(value, result)
            alpha = max(alpha, value)
        else:
            value = min(value, result)
            beta = min(beta, value)
        if alpha >= beta:
            break
    return value


def evaluate(features, weights):
    return sum(f * w for f, w in zip(features, weights))


def expected_value(payoffs, probabilities):
    return sum(v * p for v, p in zip(payoffs, probabilities))


def main():
    all_nodes = set(TREE) | set(VALUES)
    for reverse in (False, True):
        c1, c2, visited = [0], [0], []
        mm = minimax("A", True, c1, reverse)
        ab = alphabeta("A", float("-inf"), float("inf"),
                       True, c2, reverse, visited)
        order = "оңнан солға" if reverse else "солдан оңға"
        skipped = sorted(all_nodes - set(visited))
        print("Өту реті:", order)
        print("Minimax:", mm, "Түйіндер:", c1[0])
        print("Alpha-beta:", ab, "Түйіндер:", c2[0])
        print("Қысқартылған:", ", ".join(skipped) or "жоқ")
        print("Қаралған:", " -> ".join(visited))
        print()

    x, y = (8, 7, 2), (5, 5, 8)
    for weights in ((0.5, 0.3, 0.2), (0.3125, 0.1875, 0.5)):
        ex, ey = evaluate(x, weights), evaluate(y, weights)
        choice = "X" if ex > ey else "Y" if ey > ex else "тең"
        print("Салмақтар:", weights)
        print("Eval(X):", round(ex, 4), "Eval(Y):", round(ey, 4))
        print("Таңдау:", choice)

    payoffs = {"A": (8, 6, 4), "B": (3, 7, 5), "C": (2, 9, 1)}
    probs = {"A": (0.2, 0.3, 0.5), "B": (0.2, 0.5, 0.3),
             "C": (0.7, 0.2, 0.1)}
    scores = {s: expected_value(payoffs[s], probs[s]) for s in payoffs}
    worst = {s: min(payoffs[s]) for s in payoffs}
    print("Expectimax:", {s: round(v, 4) for s, v in scores.items()})
    print("Expectimax таңдауы:", max(scores, key=scores.get))
    print("Minimax таңдауы:", max(worst, key=worst.get))


if __name__ == "__main__":
    main()
