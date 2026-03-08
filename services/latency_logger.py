
import time

def measure_latency(func):

    start = time.time()

    result = func()

    end = time.time()

    latency = (end - start) * 1000

    result["latency_ms"] = latency

    print("Latency:", latency, "ms")

    return result
