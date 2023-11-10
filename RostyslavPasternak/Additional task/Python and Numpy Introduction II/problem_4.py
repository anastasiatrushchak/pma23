import math

def alt_harmonic(n):
    series = [(-1)**(i + 1) / i for i in range(1, n + 1)]
    return sum(series)


n = 500000
result = alt_harmonic(n)


ln2_approximation = math.log(2)

print(f"Sum of the first {n} terms of the alternating harmonic series: {result:.5f}")
print(f"ln(2) approximation: {ln2_approximation:.5f}")