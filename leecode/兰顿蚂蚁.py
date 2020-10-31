class Solution:
    def printKMoves(self, K: int) -> list:
        ant_position: tuple = (0, 0)
        ant_direction: int = 90
        visited: dict = {}
        move_direction: dict = {
            180: lambda x: (x[0] + 1, x[1]),
            90: lambda x: (x[0], x[1] + 1),
            0: lambda x: (x[0] - 1, x[1]),
            270: lambda x: (x[0], x[1] - 1),
        }
        letter_dict: dict = {90: 'R', 0: 'U', 270: 'L', 180: 'D'}

        for i in range(K + 1):
            ant_position = move_direction[ant_direction](ant_position)
            # print(ant_position, end=' ')
            if ant_position not in visited:
                if i != K:
                    ant_direction = (ant_direction + 90) % 360
                visited[ant_position] = 1
            else:
                if i != K:
                    ant_direction = (ant_direction - 90 if visited[ant_position] % 2 else ant_direction + 90) % 360
                visited[ant_position] += 1
            # print(ant_direction)
        # print(visited)
        standard_height: int = 0 - min(visited, key=lambda x: x[0])[0]
        standard_length: int = 0 - min(visited, key=lambda x: x[1])[1]
        height: int = max(visited, key=lambda x: x[0])[0] - min(visited, key=lambda x: x[0])[0] + 1
        length: int = max(visited, key=lambda x: x[1])[1] - min(visited, key=lambda x: x[1])[1] + 1
        map = [['_' for i in range(length)] for j in range(height)]
        # print(map)
        for i in visited:
            # print(i, [i[0] + standard_height, standard_length + i[1]])
            map[i[0] + standard_height][standard_length + i[1]] = 'X' if visited[i] % 2 else '_'
            # [print(i) for i in map]
            # print()
        # print(ant_position)
        map[ant_position[0] + standard_height][standard_length + ant_position[1]] = letter_dict[ant_direction]
        for i, _ in enumerate(map):
            map[i] = ''.join(map[i])
        return map


s = Solution()
[print(i) for i  in s.printKMoves(0)]
