# TODO Найдите количество книг, которое можно разместить на дискете
mem_mb = 1.44
mem_kb = mem_mb * 1024
mem_b = mem_kb * 1024

num_pages = 100
num_rows_per_page = 50
num_symbols_per_row = 25
mem_per_symbol = 4

total_mem_per_book = num_pages * num_rows_per_page * num_symbols_per_row * mem_per_symbol
total_books = int(mem_b/total_mem_per_book)
print("Количество книг, помещающихся на дискету:", total_books)
