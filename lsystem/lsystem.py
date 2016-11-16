rules = {
    'a': 'b',
    'b': 'ab'
}
iterations = 5
start = 'aaaaa'
end = ''
for x in range(0,iterations):
    for y in start:
        if rules[y]:
            end = end + rules[y]
    start = end
    end = ''