def calculate_structure_sum(n):
    structure_sum = 0

    def calculate(data):
        nonlocal structure_sum
        if isinstance(data, int):
            structure_sum += data
        elif isinstance(data, str):
            structure_sum += len(data)
        elif isinstance(data, (list, tuple, set)):
            for i in data:
                calculate(i)
        elif isinstance(data, dict):
            for key, value in data.items():
                calculate(key)
                calculate(value)

    calculate(n)
    return structure_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
