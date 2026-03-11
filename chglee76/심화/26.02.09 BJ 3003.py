King, Queen, Rook, Bishop, Knight, Pawn = map(int, input().split())

Chessmen = [King, Queen, Rook, Bishop, Knight, Pawn]

Chessmen_parts = [1, 1, 2, 2, 2, 8]

lack_parts = []

i = 0
for i in range(len(Chessmen)) :
    lack_parts.append(Chessmen_parts[i] - Chessmen[i])
    i += 1

print(*lack_parts)