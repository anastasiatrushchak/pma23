TOTAL_OUTLAY = 'totalOutlay'
UAH = 'uah'


def print_spends(spends):
    sum_spends(spends)
    try:
        for category, spendsInCategory in spends.items():
            if not category == TOTAL_OUTLAY:
                print("Spends in category " + category + ": ")
                for underCategory, outlay in spendsInCategory.items():
                    print("  Spends for " + underCategory + " are: " + str(outlay) + UAH)
                if TOTAL_OUTLAY in spends:
                    print("Outlay for " + category + " in this month: " + str(spends[TOTAL_OUTLAY][category]) + UAH + '\n')
                else: print("Outlay for " + category + " in this month: " + "Spends aren't summarized!\n")
            else:
                print("Total outlay in this month: " + str(spends[TOTAL_OUTLAY][TOTAL_OUTLAY]) + '\n\n')
    except Exception as err:
        print(err)


def sum_spends(month_spends):
    try:
        if TOTAL_OUTLAY in month_spends:
            month_spends.pop(TOTAL_OUTLAY)
        category_spends: dict = {}
        total_spends = 0
        for category, spendsInCategory in month_spends.items():
                sp: int = 0  # spends in category
                for underCategory, outlay in spendsInCategory.items():
                    if not isinstance(outlay, (int, float)):
                        raise TypeError(category + '/' + underCategory + ": value type must be numeric, not " + str(type(outlay)))
                    sp += outlay
                    total_spends += outlay
                category_spends[category] = sp
        category_spends[TOTAL_OUTLAY] = total_spends
        month_spends[TOTAL_OUTLAY] = category_spends
    except TypeError as t_err:
        print("TypeError in 'def sum_spends': " + str(t_err))
    except Exception as err:
        print("Error in 'def sum_spends': " + str(err))


month_spends = \
    {
        'food': {'milk': 280, 'meat': 500, 'bread': 200},
        'transport': {'tram': 160, 'taxi': 300, 'bus': 75},
        'leisure': {'cafe': 500, 'books': 200, 'youtube': 64, 'spotify': 94}
    }

print_spends(month_spends)
month_spends.pop('transport')
print_spends(month_spends)
month_spends['leisure']['books'] = 300
print_spends(month_spends)

