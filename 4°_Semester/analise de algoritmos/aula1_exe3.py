def primo(n):
    j = 2
    while j < n and n % j != 0:
        j = j + 1
    if (j == n):
        print("eh primo")
    else:
        print("nao eh primo")
print(primo(10))