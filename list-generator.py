import time
import tracemalloc

LIMIT = 10_000_000


def get_squares_list(n):
    squares = []
    for i in range(n):
        squares.append(i * i)
    return squares


def get_squares_gen(n):
    for i in range(n):
        yield i * i


# List Version
tracemalloc.start()
start_time = time.time()

my_list = get_squares_list(LIMIT)
total_sum_list = sum(my_list)

end_time = time.time()
current_mem, peak_mem = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("--- List Version ---")
print(f"Time taken: {end_time - start_time:.4f} seconds")
print(f"Peak memory usage: {peak_mem / 1048576:.2f} MB")

# Generator Version
tracemalloc.start()
start_time = time.time()

gen_obj = get_squares_gen(LIMIT)
total_sum_gen = sum(gen_obj)

end_time = time.time()
current_mem, peak_mem = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("\n--- Generator Version ---")
print(f"Time taken: {end_time - start_time:.4f} seconds")
print(f"Peak memory usage: {peak_mem / 1048576:.2f} MB")