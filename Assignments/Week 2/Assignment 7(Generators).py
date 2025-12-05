# Task 1
print("\n------------Task 1------------\n") 
def fibonacci_generator():
    a=0
    b=1
    while True:
        yield a
        c=a+b
        a=b
        b=c

gen = fibonacci_generator()
for i in range(0,10):
    print(next(gen))

# Task 2
print("\n------------Task 2------------\n") 
def multiple_generator(n):
    i=1
    while True:
        yield n*i
        i+=1

gen = multiple_generator(3)
for i in range(5):
    print(next(gen))

# Task 3
print("\n------------Task 3------------\n") 
def repeat_word(word, times):
    for ch in word:
        for _ in range(times):
            yield ch
            
word = "hello"
times = 5
print(''.join(repeat_word(word, times)))