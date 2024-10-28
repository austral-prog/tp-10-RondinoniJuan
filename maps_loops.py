def find_max_value(dict):
    if dict != {}:
        return max(dict, key=dict.get)

    else:
        return ""

def reverse_dict(dict):
    reversed_dict = {}

    for key, value in dict.items():
        if value in reversed_dict:
            reversed_dict[value] += key

        else:
            reversed_dict[value] = key

    return reversed_dict

def word_freq_counter(words):
    frequency_dict = {}

    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict

def find_biggest_expense(dict):
    max_average = 0
    max_expense = ""

    for item, costs in dict.items():
        avg_cost = sum(costs) / len(costs) if costs else 0

        if avg_cost > max_average:
            max_average = avg_cost
            max_expense = item

    return max_expense

def sum_of_expenses(expenses):
    total_expenses = {item: sum(costs) for item, costs in expenses.items()}

    return total_expenses

def sum_of_expenses_by_type(expenses):
    type_sums = {}

    for item, cost_pairs in expenses.items():
        for type_, cost in cost_pairs:
            type_sums[type_] = type_sums.get(type_, 0) + cost

    return type_sums
