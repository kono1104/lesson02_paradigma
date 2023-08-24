from collections import deque



def find_path(maze, start, end):

    rows = len(maze)

    cols = len(maze[0])

    

    # Создаем массив для хранения посещенных ячеек

    visited = [[False] * cols for _ in range(rows)]

    

    # Создаем массив для хранения предыдущих ячеек

    prev = [[None] * cols for _ in range(rows)]

    

    # Определяем смещения для перехода в соседние ячейки

    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    

    # Ставим начальную точку в очередь

    queue = deque([start])

    

    # Помечаем начальную точку как посещенную

    visited[start[0]][start[1]] = True

    

    while queue:

        x, y = queue.popleft()

        

        # Если текущая ячейка - конечная, то построим путь

        if (x, y) == end:

            path = []

            while (x, y) != start:

                path.append((x, y))

                x, y = prev[x][y]

            path.append(start)

            path.reverse()

            return path

        

        # Проверяем соседние ячейки

        for dx, dy in offsets:

            nx, ny = x + dx, y + dy

            

            # Проверяем, что ячейка внутри лабиринта и является проходом

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '0' and not visited[nx][ny]:

                queue.append((nx, ny))

                visited[nx][ny] = True

                prev[nx][ny] = (x, y)

    

    # В случае, если путь не найден

    return None
maze = [

    ['0', '1', '0', '0', '0'],

    ['0', '1', '0', '1', '0'],

    ['0', '0', '0', '1', '0'],

    ['0', '1', '0', '0', '0'],

    ['0', '0', '0', '0', '0']

]



start = (0, 0)

end = (4, 4)



path = find_path(maze, start, end)



if path:

    print("Путь найден:")

    for x, y in path:

        print(f"({x}, {y})")

else:

    print("Путь не найден")