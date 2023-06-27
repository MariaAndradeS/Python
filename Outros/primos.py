def contador(start, end):
    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False

    for number in range(2, int(end ** 0.5) + 1):
        if is_prime[number]:
            for multiple in range(number * number, end + 1, number):
                is_prime[multiple] = False

    prime_count = 0
    non_prime_count = 0
    for number in range(start, end + 1):
        if is_prime[number]:
            prime_count += 1
        else:
            non_prime_count += 1

    return prime_count, non_prime_count

start = int(input("Digite o número de inicio: "))
end = int(input("Digite o número de fim: "))

prime_count, non_prime_count = contador(start, end)

print("Quantidade de números primos:", prime_count)
print("Quantidade de números não primos:", non_prime_count)