from operator import itemgetter
from texttable import Texttable

data = [
        (34, "ABC"),
        (23, "ACB"),
        (26, "BAC"),
        (2, "BCA"),
        (13, "CAB"),
        (11, "CBA")
        ]

def borda(candidate):

    def borda_score(data_record):
        (voters, prefs) = data_record
        multiplier = len(prefs) - prefs.index(candidate)
        return voters * multiplier

    return sum(map(borda_score, data))

scores = list(map(lambda c: (c, borda(c)), "ABC"))

table = Texttable()
table.header(["Кандидат", "Оцінка"])
list(map(lambda x: table.add_row([x[0], x[1]]), scores))
print(table.draw())

(best_candidate, best_score) = max(scores, key = itemgetter(1))

print("Переможець: кандидат", best_candidate)


