import multiprocessing
import pathlib
import random
import typing as tp

import numpy

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ На вход подается имя файла, на выходе получаем поле судоку """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Получает на вход вложенный список судоку, вывод его в виде таблицы """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировывает значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return [list(array) for array in numpy.array_split(values, n)]


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Получает список строк судоку и номер строки, возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Получает список строк судоку и номер столбца, возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    return [number[pos[1]] for number in grid]


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Получает вложенный список судоку и номер ячейки, возвращает все значения из квадрата, в который попадает позиция ячейки pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    if pos[0] <= 2:
        rows = [0, 3]
    elif pos[0] <= 5:
        rows = [3, 6]
    elif pos[0] <= 8:
        rows = [6, 9]
    if pos[1] <= 2:
        cols = [0, 3]
    elif pos[1] <= 5:
        cols = [3, 6]
    elif pos[1] <= 8:
        cols = [6, 9]
    return [grid[row][col] for row in range(rows[0], rows[1]) for col in range(cols[0], cols[1])]


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Получает на вход судоку и находит первую свободную позицию в пазле, возвращает ее координаты
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '.':
                return (row, col)


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Получает на вход судоку и коорбинату свободной ячейки, возвращает множество возможных значений для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    square = get_block(grid, pos)
    column = get_col(grid, pos)
    string = get_row(grid, pos)
    values = set()
    for i in range(1, 10):
        if str(i) not in square and str(i) not in column and str(i) not in string:
            values.add(str(i))
    return values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """ Решение пазла, заданного в grid, возвращение решенного судоку
    Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    empty_pos = find_empty_positions(grid)
    if not empty_pos:
        return grid
    row, col = empty_pos
    for i in range(1, 10):
        if str(i) in find_possible_values(grid, empty_pos):
            grid[row][col] = str(i)
            if solve(grid) != 0:
                return grid
            grid[row][col] = '.'
    return 0


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Получает на вход решенное судоку, проверяет на правильность. Если решение solution верно, то возвращает True, в противном случае False
    >>> check_solution([['5', '3', '5', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']])
    False
    >>> check_solution([['5', '3', '5', '6', '7', '8', '9', '1', '2'], ['6', '6', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']])
    False
    """
    count_goals = 0
    if_solved = 0
    for i in range(9):
        for j in range(9):
            if solution[i][j].isdigit():
                if_solved += 1
    if if_solved == 81:
        for i in solution:
            if len(i) == len(set(i)):
                count_goals += 1
        for i in range(9):
            check_cols = get_col(solution, (0, i))
            if len(check_cols) == len(set(check_cols)):
                count_goals += 1
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                check_blocks = get_block(solution, (i, j))
                if len(check_blocks) == len(set(check_blocks)):
                    count_goals += 1
    if count_goals == 27:
        return True
    return False


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Получает на вход количество заполненных ячеек N и генерирует судоку, заполненный на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    empty_sudoku = [['.' for i in range(9)] for j in range(9)]
    solved_sudoku = solve(empty_sudoku)
    while sum(1 for string in solved_sudoku for cell in string if cell == '.') < (81 - N):
        row, col = random.randint(0, 8), random.randint(0, 8)
        solved_sudoku[row][col] = '.'
    return solved_sudoku


def run_solve(filename: str) -> None:
    grid = read_sudoku(filename)
    display(grid)
    solution = solve(grid)
    if not solution:
        print(f"Puzzle {filename} can't be solved")
    else:
        display(solution)


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        p = multiprocessing.Process(target=run_solve, args=(fname,))
        p.start()
