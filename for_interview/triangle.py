def get_triangle_kind(a, b, c):
    if a == b == c:
        return "Равносторонний"

    if a == b or b == c or c == a:
        return "Равнобедренный"

    return "Разносторонний"


print(get_triangle_kind(1, 3, 2)) # "Разносторонний"
print(get_triangle_kind(14, 14, 18)) # "Равнобедренный"
print(get_triangle_kind(10, 10, 10)) # "Равносторонний"