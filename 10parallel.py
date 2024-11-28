import multiprocessing

# Function to calculate the sum of squares for a chunk of numbers
def sum_of_squares(numbers, result, index):
    total = sum(x * x for x in numbers)
    result[index] = total

# Function to calculate the sum of squares in parallel
def parallel_sum_of_squares(numbers, num_processes):
    chunk_size = len(numbers) // num_processes
    chunks = [numbers[i * chunk_size: (i + 1) * chunk_size] for i in range(num_processes)]

    # Handle remaining numbers if not evenly divisible
    if len(numbers) % num_processes != 0:
        chunks[-1].extend(numbers[num_processes * chunk_size:])

    # Shared array to store results from each process
    result = multiprocessing.Array('i', num_processes)
    processes = []

    # Create processes to compute sum of squares for each chunk
    for i in range(num_processes):
        p = multiprocessing.Process(target=sum_of_squares, args=(chunks[i], result, i))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    # Combine results from all processes
    total_sum = sum(result)
    return total_sum

if __name__ == '__main__':
    n = int(input("How many numbers? "))
    numbers = list(range(1, n + 1))
    num_processes = multiprocessing.cpu_count()  # Use all available CPU cores

    total = parallel_sum_of_squares(numbers, num_processes)
    print(f"The sum of squares is: {total}")
