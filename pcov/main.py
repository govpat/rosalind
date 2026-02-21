from collections import defaultdict


def eulerian_cycle(graph, start):
    local = {u: list(vs) for u, vs in graph.items()}
    stack = [start]
    path = []
    while stack:
        u = stack[-1]
        if local.get(u):
            stack.append(local[u].pop())
        else:
            path.append(stack.pop())
    return path[::-1]


def assemble_pcov(kmers):
    graph = defaultdict(list)
    indeg = defaultdict(int)
    outdeg = defaultdict(int)
    for k in kmers:
        a, b = k[:-1], k[1:]
        graph[a].append(b)
        outdeg[a] += 1
        indeg[b] += 1
        if b not in graph:
            graph[b] = graph[b]

    start = sorted(graph.keys())[0]
    for u in sorted(graph.keys()):
        if outdeg[u] > 0:
            start = u
            break

    cyc = eulerian_cycle(graph, start)
    if len(cyc) < 2:
        return ''

    # For circular perfect coverage, return one character per edge in the cycle.
    return ''.join(node[0] for node in cyc[:-1])


def main():
    with open('rosalind_pcov.txt', 'r') as f:
        kmers = [line.strip() for line in f if line.strip()]
    print(assemble_pcov(kmers))


if __name__ == '__main__':
    main()
