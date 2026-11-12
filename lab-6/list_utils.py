# Модуль list_utils: функції для роботи зі списками

def sort_list(lst):
    return sorted(lst)

def remove_duplicates(lst):
    return list(set(lst))

def min_max(lst):
    return min(lst), max(lst)
