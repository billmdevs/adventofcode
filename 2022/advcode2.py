'''
def score(p1, p2):
    if (p1 - 1) % 3 == p2:
        return p2 + 1
    elif (p2 - 1) % 3 == p1:
        return p2 + 7
    return p2 + 4


with open("input_files/day02", "r") as f:
    data = f.read().splitlines()
    data = [line.split() for line in data]
    data = [(ord(p1) - ord("A"), ord(p2) - ord("X")) for p1, p2 in data]

moves = [(p1, (p1 + p2 - 1) % 3) for p1, p2 in data]

print(sum(score(p1, p2) for p1, p2 in data))
print(sum(score(p1, p2) for p1, p2 in moves))
'''

with open("input_files/day2") as fp:
	rounds = fp.read().strip().splitlines()

#print(rounds)

outcomes = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6,}

# Part 1
total_points_p1 = 0
for r in rounds:
	total_points_p1 += outcomes[r]

print("Answers to part 1: ", total_points_p1)
