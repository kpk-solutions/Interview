import threading
import time

urls = ["https://github.com", "https://spacexdata.com", "https://zippopotam.us"]
def fecth_data(url):
    print(f'Fetching data from {url}')
    time.sleep(1)
    print('Data fetched')
start = time.time()

threads = []
for url in urls:
    t = threading.Thread(target=fecth_data, args=(url,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print(f'Total time: {time.time() - start}')

import multiprocessing as mp

def kitchen_worker(kitchen_id, dish_name):
    print(f"Kitchen-{kitchen_id}: Starting to cook {dish_name}...\n")
    time.sleep(1)
    print(f"Kitchen-{kitchen_id}: Successfully finished cooking {dish_name}!\n")

if __name__ == '__main__':
    orders = ["Paradise Biryani", "Masala Dosa", "Irani Chai"]
    active_kitchens = []
    start_time = time.time()
    for index, dish in enumerate(orders):
        kitchen_number = index + 1
        p = mp.Process(target=kitchen_worker, args=(kitchen_number, dish))
        active_kitchens.append(p)
        p.start()
