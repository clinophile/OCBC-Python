

'''Read File'''
try:
    f = open("sample.txt", encoding='utf-8')
    print(f.read())
    # perform file operations
finally:
    f.close()

'''Write File'''
# w = write
with open("sample2.txt", 'w', encoding='utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")


print("========================================")
try:
    f = open("sample.txt", 'r', encoding='utf-8')
    print(f.read())
finally:
    f.close()

print("========================================")
try:
    f = open("sample.txt", 'r', encoding='utf-8')
    print(f.readline())
finally:
    f.close()
