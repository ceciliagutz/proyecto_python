import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

import httpx

URLS = [
    "https://example.com",
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/posts/1",
] * 3


# VERSION SYNc
def fetch_sync(urls):
    results = []
    with httpx.Client() as client:
        for url in urls:
            response = client.get(url)
            results.append(response.status_code)
    return results


# Version ASYNC


async def fetch_one(client, url, semaphore):
    async with semaphore:
        response = await client.get(url)
        return response.status_code


async def fetch_async(urls):
    semaphore = asyncio.Semaphore(3)
    async with httpx.AsyncClient() as client:
        tasks = [fetch_one(client, url, semaphore) for url in urls]
        return await asyncio.gather(*tasks)


# CPU-bound multiprocessing
def heavy_computation(n):
    total = 0
    for i in range(10_000_000):
        total += i * n
    return total


def run_cpu_tasks():
    numbers = [1, 2, 3, 4]
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(heavy_computation, numbers))
    return results


# Time compare


def main():
    print("Comparing synchronous vs asynchronous fetch")

    # Synchronous
    start = time.time()
    fetch_sync(URLS)
    sync_time = time.time() - start
    print(f"Synchronous: {sync_time:.2f} seconds")

    # Asynchronous
    start = time.time()
    asyncio.run(fetch_async(URLS))
    async_time = time.time() - start
    print(f"Asynchronous: {async_time:.2f} seconds")

    # CPU-bound
    print("\nExecuting CPU-bound tasks")
    start = time.time()
    run_cpu_tasks()
    cpu_time = time.time() - start
    print(f"CPU-bound: {cpu_time:.2f} seconds")


if __name__ == "__main__":
    main()
