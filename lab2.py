from operator import itemgetter
from texttable import Texttable

def a_calc(n, p1, p2):
    m1 = 730
    d1 = 200
    d2 = -75
    return (["А"], n * (p1 * d1 + p2 * d2) - m1)

a = a_calc(5, 0.75, 0.25)

def b_calc(n, p1, p2):
    m2 = 180
    d1 = 150
    d2 = -40
    return (["Б"], n * (p1 * d1 + p2 * d2) - m2)

b = b_calc(5, 0.75, 0.25)

def c_calc():
    p3 = 0.7
    p4 = 0.3
    p1 = 0.85
    p2 = 0.15
    c_a = a_calc(4, p1, p2)
    c_b = b_calc(4, p1, p2)
    print("BA", c_a, "BБ", c_b)
    (branch, revenue) = max([c_a, c_b], key = itemgetter(0))
    return (["В"] + branch, p3 * revenue)

c = c_calc()

print(a, b, c)
(branch, revenue) = max([a, b, c], key = itemgetter(0))
print("Найкращий варіант:", branch)
print("Очікуваний прибуток:", revenue, "тис. доларів")
