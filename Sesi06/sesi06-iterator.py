def my_generator():
  print("Inside my generator")
  yield 'a'
  yield 'b'
  yield 'c'

for char in my_generator():
  print(char)

print(my_generator())

print("==================================")

store_generator = my_generator()
print(next(store_generator))
print(next(store_generator))


print("======================")

def counter_generator(low, high):
    while low <= high:
       yield low
       low += 1

for i in counter_generator(5,10):
  print(i, end=' ')


print("\n========================")

#list comprehension
squared_nums = [y*y for y in [1,2,3,4,5]]

print(squared_nums)

print("========================")



# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1

# for i in infinite_sequence():
#   print(i, end=" ")
