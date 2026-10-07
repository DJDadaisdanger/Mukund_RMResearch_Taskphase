import random
board = [['~'] * 8 for _ in range(8)]
available_coords = {(x, y) for x in range(8) for y in range(8)}

for size in [6, 4, 2]:
    valid_placements = []

    for x in range(8):
        for y in range(8):
            if y + size <= 8:
                h_pos = {(x, y + i) for i in range(size)}
                if h_pos.issubset(available_coords):
                    valid_placements.append(h_pos)

            if x + size <= 8:
                v_pos = {(x + i, y) for i in range(size)}
                if v_pos.issubset(available_coords):
                    valid_placements.append(v_pos)

    chosen_placement = random.choice(valid_placements)
    available_coords -= chosen_placement

hits, tries, guessed = 0, 0, set()

print('\n'.join([' '.join(row) for row in board]))

while hits < 12:
    try:
        x, y = map(int, input("\nStrike (row col): ").split())
        if 0 <= x <= 7 and 0 <= y <= 7 and (x, y) not in guessed:
            guessed.add((x, y))
            tries += 1

            if (x, y) not in available_coords:
                board[x][y] = 'X'
                hits += 1
                print("HIT!")
            else:
                board[x][y] = 'O'
                print("MISS!")

            print('\n'.join([' '.join(row) for row in board]))
    except:
        pass

print(f"\nVictory! Fleet destroyed in {tries} strikes.")