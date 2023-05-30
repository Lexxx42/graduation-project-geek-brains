# отсортировать сначала четные, затем нечетные элементы

generated_list = [1, 54, 455, 21, 13, 6, 0, 8]

print(generated_list)

sorted_list = ()

print(sorted(filter(lambda x: not 2, generated_list)) + sorted(filter(lambda x: 2, generated_list)))
