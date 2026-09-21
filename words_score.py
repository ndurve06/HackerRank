n = int(input())
sentence = input().lower().split()
vowels = "aeiouy"

score = 0

for word in sentence:
    count = sum(1 for ch in word if ch in vowels)
    if count % 2 == 0:
        score += 2
    else:
        score += 1

print(score)