start = 10
end = 50

print(f"Bilangan prima antara {start} dan {end} adalah:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)