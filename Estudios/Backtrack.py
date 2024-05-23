# 1. 

def permute(longitud, lista):
    if longitud == 1:
        return lista
    else:
        return [x + y for x in permute(1, lista) for y in permute(longitud-1, lista)]
    
# 2. 

candidates = [3, 4, 5, 6, 9]
target = 9

def combinationSum(candidates, target) -> list[list[int]]:
    if not candidates or min(candidates) > target:
        return[]
    
    def inner_combinationSum(nums, index, tar, path, result):
        if tar == 0 and path not in result:
            result.append(path)
            return
        elif tar < 0 or index >= len(nums):
            return
        
        for i in range(index, len(nums)):
            inner_combinationSum(candidates, i + 1, tar - nums[i], path + [nums[i]], result)
    
    result = []

    inner_combinationSum(candidates, 0, target, [], result)

    return result

# 3. 

board = [[3, 0, 0, 8, 0, 1, 0, 0, 2],
         [2, 0, 1, 0, 3, 0, 6, 0, 4],
         [0, 0, 0, 2, 0, 4, 0, 0, 0],
         [8, 0, 9, 0, 0, 0, 1, 0, 6],
         [0, 6, 0, 0, 0, 0, 0, 5, 0],
         [7, 0, 2, 0, 0, 0, 4, 0, 9],
         [0, 0, 0, 5, 0, 9, 0, 0, 0],
         [9, 0, 4, 0, 8, 0, 7, 0, 5],
         [6, 0, 0, 1, 0, 7, 0, 0, 3]]

def print_board(board):
    print("-" * 37)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |" * 3).format(*[x if x != 0 else " " for x in row]))
        if i == 8:
            print("-" * 37)
        elif i%3 == 2:
            print("|" + "---+"*8 + "---|")
        else:
            print("|" + "---+"*8 + "---|")

def validate(board, row, col, number):
    def is_valid_row():
        return number not in board[row]
    
    def is_valid_col():
        return number not in [row[col] for row in board ]
    
    def is_valid_3x3():
        pos_x = col//3 * 3
        pos_y = row//3 * 3
        lst = []

        for i in range(pos_y, pos_y + 3):
            lst.extend(board[i][pos_x:pos_x+3])

    return is_valid_row() and is_valid_col() and is_valid_3x3()

if __name__ == "__main__":
    print(validate(board, 0, 1, 5))
