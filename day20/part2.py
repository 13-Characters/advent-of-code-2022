input = open("input.txt").readlines()
input = [int(x) * 811589153 for x in input] # This line changes

indices = list(range(len(input)))
reshuffledInput = input.copy()
reshuffledInput = [int(x) for x in reshuffledInput]
for count in range(10): # new loop
    for h, line in enumerate(input):
        i = indices.index(h)
        reshuffledInput.pop(i)
        indices.pop(i)
        if i + line == 0:
            if line > 0:
                reshuffledInput.insert(0, line)
                indices.insert(0, h)
            else:
                reshuffledInput.insert(len(reshuffledInput), line)
                indices.insert(len(indices), h)
        else:
            reshuffledInput.insert((i + line) % (len(reshuffledInput)), line)
            indices.insert((i + line) % (len(indices)), h)

zeroIndex = reshuffledInput.index(0)
result = reshuffledInput[(zeroIndex + 1000) % len(reshuffledInput)] \
         + reshuffledInput[(zeroIndex + 2000) % len(reshuffledInput)] \
         + reshuffledInput[(zeroIndex + 3000) % len(reshuffledInput)]
print(result)



