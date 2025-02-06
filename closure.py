from typing import Callable

def make_multiplier_of(n):

    def multiplier(y):
        return y * n

    return multiplier

times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)

print(times3(3))
print(times5(8))
print(times3(times5(2)))

def produce(device_name: str) -> Callable:
    count = 0

    def device():
        nonlocal count
        count += 1
        print(f"{device_name} launch {count}")
    return device
cell_phone = produce("Cell Phone")
laptop = produce("Laptop")
cell_phone()
cell_phone()
cell_phone()
laptop()
laptop()
cell_phone()
