def count_in_list(lst: list[str], string: str) -> int:
    return sum([1 for s in lst if s == string])
