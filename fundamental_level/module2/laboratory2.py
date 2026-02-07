import random
import time
from contextlib import contextmanager

# Reintentar una funcion silla


def retry(max_attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay

            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Error: {e}. Retrying in {current_delay} seconds...")
                    time.sleep(current_delay)
                    current_delay *= 2  # backoff
            raise Exception("Max attempts reached")

        return wrapper

    return decorator


# Test function of the decorator


@retry(max_attempts=3, delay=1)
def unstable_function():
    if random.random() < 0.7:
        raise ValueError("Random failure")
    print("Function succeeded")


# Batch generator


def batch_generator(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i : i + batch_size]


numbers = list(range(1, 11))

print("\nBatches:")
for batch in batch_generator(numbers, 3):
    print(batch)

# timing context manager


@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Execution time: {end - start:.2f} seconds ")


print("\nTiming example:")
with timer():
    time.sleep(2)

print("Testing retry decorator:")
try:
    unstable_function()
except Exception as e:
    print("Final error:", e)
