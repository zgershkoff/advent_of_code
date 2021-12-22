from collections import defaultdict

class Maze():
    def __init__(self, filename='inputs/day12.txt'):
        self.graph = defaultdict(list)
        with open(filename, 'r') as f:
            for line in f.readlines():
                u, v = line.strip().split('-')
                self.graph[u].append(v)
                self.graph[v].append(u)

    def dfs(self):
        count = 0
        path = ['start']

        def dfs_step():
            nonlocal count
            nonlocal path
            cur_vertex = path[-1]
            if cur_vertex == 'end':
                path.pop()
                count += 1
                return
            for v in self.graph[cur_vertex]:
                if v not in path or v.isupper():
                    path.append(v)
                    dfs_step()
            path.pop()

        dfs_step()
        return count

    def dfs2(self):
        count = 0
        path = ['start']
        small_twice = False
        seen_twice = ''

        def dfs_step():
            nonlocal count, path, small_twice, seen_twice
            cur_vertex = path[-1]
            if cur_vertex == 'end':
                # print(path)
                path.pop()
                count += 1
                return
            for v in self.graph[cur_vertex]:
                if v != 'start':
                    vcount = path.count(v)
                    if v.isupper() or (vcount < 1 or not small_twice):
                        if v.islower() and (vcount == 1 and not small_twice):
                            small_twice = True
                            seen_twice = v
                        path.append(v)
                        dfs_step()

            last_vertex = path.pop()
            if last_vertex == seen_twice:
                small_twice = False

        dfs_step()
        return count

if __name__ == "__main__":
    M = Maze('inputs/day12.txt')
    print(M.dfs())
    print(M.dfs2())


