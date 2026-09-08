from math import factorial, comb

# 1.38
total_permutations = factorial(5)
p_1_38 = 1 / total_permutations
print(f"1.38 1/5! = {p_1_38:.6f}")

# 1.43 — Телефонный номер из 5 цифр (не начинается с 0)
total_numbers = 9 * 10**4

# а) Все цифры различные
favorable_a = 9 * 9 * 8 * 7 * 6
p_1_43_a = favorable_a / total_numbers
print(f"1.43 а) (9*9*8*7*6)/(9*10^4) = {p_1_43_a:.6f}")

# б) Все цифры одинаковые
favorable_b = 9
p_1_43_b = favorable_b / total_numbers
print(f"1.43 б) 9/(9*10^4) = {p_1_43_b:.6f}")

# в) Все цифры нечетные
favorable_v = 5**5
p_1_43_v = favorable_v / total_numbers
print(f"1.43 в) 5^5/(9*10^4) = {p_1_43_v:.6f}")

# 1.48 — Бросание трех игральных костей
total_dice = 6**3

# а) Выпадение 11 очков
count_11 = 0
for d1 in range(1, 7):
    for d2 in range(1, 7):
        for d3 in range(1, 7):
            if d1 + d2 + d3 == 11:
                count_11 += 1
p_1_48_a = count_11 / total_dice
print(f"1.48 а) {count_11}/6^3 = {p_1_48_a:.6f}")

# б) Выигрыш (сумма > 10)
count_win = 0
for d1 in range(1, 7):
    for d2 in range(1, 7):
        for d3 in range(1, 7):
            if d1 + d2 + d3 > 10:
                count_win += 1
p_1_48_b = count_win / total_dice
print(f"1.48 б) {count_win}/6^3 = {p_1_48_b:.6f}")