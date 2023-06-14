from counter import Counter
tally = Counter()
tally.reset()
tally.click()
tally.click()

result = tally.getValue()
print(f'Value: {result}')

tally.click()
result = tally.getValue()
print(f'Value: {result}')