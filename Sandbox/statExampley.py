import statistics

numbers =[1, 2, 5, 3, 4, 5, 4, 5, 5, 6]

op = input('enter function name :')

if op == 'mean':
    print( statistics.mean(numbers))
elif op == 'mode':
    print(  statistics.mode(numbers))
elif op == 'median':
    print(  statistics.median(numbers))
elif op == 'min':
    print(  min(numbers))
elif op == 'max':
    print(  max(numbers))
elif op == 'range':
    print(  max(numbers) - min(numbers))
else:
    print(  average(numbers, 'mean'))
    


