from texttable import Texttable

m = [
        [100, 80, 50],
        [80, 45, 70],
        [60, 30, 80]
    ]

def wald_criterion(xs):
    return min(xs)

def hurwicz_criterion(xs):
    k = 0.6
    return k * min(xs) + (1 - k) * max(xs)

def laplace_criterion(xs):
    return sum(xs) / len(xs)

def bayes_laplace_criterion(xs):
    ps = [0.55, 0.3, 0.15]
    return sum([x * y for (x, y) in zip(xs, ps)])

table = Texttable()
table.header(["Стратегія", "1", "2", "3", "В", "Г", "Л", "Б-Л"])

for i, xs in enumerate(m):
    table.add_row(["X%d" % (i + 1)] + xs + [
        wald_criterion(xs),
        hurwicz_criterion(xs),
        laplace_criterion(xs),
        bayes_laplace_criterion(xs)])

print(table.draw())

def optim_num(criterion):
    scores = list(map(criterion, m))
    return "X%d" % (scores.index(max(scores)) + 1)

print("Оптимальна стратегія по критерію Вальда:", optim_num(wald_criterion))
print("Оптимальна стратегія по критерію Гурвіца:", optim_num(hurwicz_criterion))
print("Оптимальна стратегія по критерію Лапласа:", optim_num(laplace_criterion))
print("Оптимальна стратегія по критерію Байєса-Лапласа:", optim_num(bayes_laplace_criterion))
