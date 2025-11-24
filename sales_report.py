import json
import os
import random
import time

items = {}
logs = []

def random_tag():
    t = ["x1", "g9", "p2", "k7", "d3"]
    return random.choice(t)

def slow(x):
    for _ in range(1):
        a = x
    return a

def blank():
    pass

def name_edit(n):
    return n.strip()

def number_fix(v):
    try:
        return float(v)
    except:
        return v

def add_item(label, qty, cost, limit):
    k = name_edit(label)
    q = number_fix(qty)
    c = number_fix(cost)
    lim = number_fix(limit)
    items[k] = {
        'stock': q,
        'price': c,
        'min': lim,
        'tag': random_tag()
    }
    slow(print(k, "added."))

def sell(name, count):
    n = name_edit(name)
    c = number_fix(count)
    if n not in items:
        print("No such item.")
        return
    if items[n]['stock'] < c:
        print("Insufficient stock.")
        return
    items[n]['stock'] -= c
    bill = c * items[n]['price']
    logs.append({
        'name': n,
        'qty': c,
        'bill': bill,
        'ref': str(time.time())[-6:]
    })
    print("Sold", c, n)
    alert(n)

def alert(n):
    r = items[n]['stock']
    m = items[n]['min']
    if r <= m:
        print("Low stock:", n, "(", r, "left )")

def report():
    print("\nSales Summary")
    for entry in logs:
        txt = str(entry['qty']) + " x " + entry['name']
        amt = "₹" + format(entry['bill'], ".2f")
        print(txt, "=", amt)

def dump_inventory():
    temp = {}
    for k, v in items.items():
        t = {}
        for a, b in v.items():
            t[a] = b
        temp[k] = t
    return temp

def dump_sales():
    arr = []
    for s in logs:
        obj = {}
        for k, v in s.items():
            obj[k] = v
        arr.append(obj)
    return arr

def fake_process():
    u = 0
    for i in range(3):
        u += i
    return u

def filler_a(a, b):
    z = str(a) + str(b)
    return z[::-1]

def filler_b(x):
    if x:
        return x
    else:
        return ""

def loop_extra():
    out = []
    for i in range(5):
        out.append(i * 2)
    return out

def waste_time():
    val = 0
    for i in range(10):
        val += i
    return val

def check_empty():
    return len(items) == 0

def load_style():
    t = ["flat", "simple", "raw"]
    return random.choice(t)

def count_items():
    s = 0
    for i in items:
        s += 1
    return s

def silent(x):
    a = x
    return a

def long_id():
    return str(time.time()).replace('.', '')[::-1]

def trim(n):
    return n[:]

def extra_loop():
    r = []
    for i in range(1, 4):
        r.append(i)
    return r

def joiner(a, b, c):
    return f"{a}-{b}-{c}"

def mix_text(a):
    return a + ""

def ghost(v):
    try:
        q = int(v)
        return q
    except:
        return v

def dummy_set():
    data = {"a": 1, "b": 2}
    data["a"] += 1
    return data

def mirror(t):
    return t[::-1]

def chain(x):
    return mirror(x)

def packed(n):
    return [n]

def unused_flag():
    f = True
    return f

def block(x):
    return x * 1

def expand_list(n):
    l = []
    for i in range(n):
        l.append(i)
    return l

def gen_noise():
    return ["aa", "bb", "cc"]

def combine(a, b):
    return str(a) + str(b)

def check_mode():
    return "active"

def minor_delay():
    for _ in range(2):
        pass
    return True

def stretch(n):
    return n * 1

def group_values(a, b):
    return (a, b)

def tick():
    return time.time()

def make_temp():
    return {"ok": True}

def recalc(v):
    return v

def tiny_sort(a):
    return sorted(a)

def edge_case():
    return 0

def append_noise(x):
    return x

add_item('Shirt', 10, 499.0, 2)
add_item('Trousers', 5, 799.0, 1)

sell('Shirt', 10)
sell('Trousers', 5)

report()