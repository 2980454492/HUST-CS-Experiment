import random


class Sudoku:
    def __init__(self, size=9):
        self.size = size
        self.board = [[0] * size for _ in range(size)]

    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) if num != 0 else '.' for num in row))

    def is_valid(self, row, col, num):
        # 行检查
        if num in self.board[row]:
            return False
            # 列检查
        if num in [self.board[r][col] for r in range(self.size)]:
            return False
            # 3x3 宫检查
        box_row_start = (row // 3) * 3
        box_col_start = (col // 3) * 3
        for r in range(box_row_start, box_row_start + 3):
            for c in range(box_col_start, box_col_start + 3):
                if self.board[r][c] == num:
                    return False
        return True

    def fill_board(self):
        nums = list(range(1, 10))
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:  # 仅在空白处填充
                    random.shuffle(nums)
                    for num in nums:
                        if self.is_valid(i, j, num):
                            self.board[i][j] = num
                            if self.fill_board():  # 递归调用
                                return True
                            self.board[i][j] = 0  # 回溯
                    return False  # 如果没有数字可以填充，返回 False
        return True  # 如果所有位置都已填充

    def generate_board(self, filled_cells=36):
        self.fill_board()
        for _ in range(self.size * self.size - filled_cells):
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            while self.board[row][col] == 0:
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)
            self.board[row][col] = 0

    def is_complete(self):
        return all(all(num != 0 for num in row) for row in self.board)

    def solve(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid(i, j, num):
                            self.board[i][j] = num
                            if self.solve():
                                return True
                            self.board[i][j] = 0
                    return False
        return True


def main():
    sudoku = Sudoku()

    print("输入1，自动生成数独初盘\n输入2，人工设置初盘")
    op=input()
    if op=="1":
        # 生成数独初盘
        print("生成的数独初盘：")
        sudoku.generate_board()
        sudoku.print_board()

    elif op=="2":
        # 人工设置初盘
        print("\n请设置数独初盘，输入空格用 '.' 表示，输入完成后回车:")
        for i in range(sudoku.size):
            line = input(f"第{i + 1}行: ").strip().replace('.', '0').split()
            for j in range(sudoku.size):
                num = int(line[j]) if line[j] != '0' else 0
                sudoku.board[i][j] = num

                # 检测人工设置的合法性
        valid = True
        for i in range(sudoku.size):
            for j in range(sudoku.size):
                if sudoku.board[i][j] != 0 and not sudoku.is_valid(i, j, sudoku.board[i][j]):
                    valid = False
                    break
            if not valid:
                break

        if valid:
            print("\n初盘合法！")
            sudoku.print_board()
        else:
            print("\n初盘不合法！")

        # 求解数独
    if sudoku.solve():
        print("\n求解后的数独：")
        sudoku.print_board()
    else:
        print("无法求解该数独。")


if __name__ == "__main__":
    main()