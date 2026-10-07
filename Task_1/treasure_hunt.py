def find_treasure(grid):
    x, y = 1, 1
    
    while True:
        val = grid[x - 1][y - 1]
        print("Visited (" + str(x) + ", " + str(y) + ") -> Clue: " + str(val))
        
        if val == x * 10 + y:
            print("Treasure found at (" + str(x) + ", " + str(y) + ")")
            break
            
        val_str = str(val)
        x = int(val_str[0])
        y = int(val_str[1])

def main():
    treasure_map = [
        [34, 21, 32, 41, 25],
        [14, 42, 43, 14, 31],
        [54, 45, 52, 42, 23],
        [33, 15, 51, 31, 35],
        [21, 52, 33, 13, 23]
    ]
    
    find_treasure(treasure_map)

main()