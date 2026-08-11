import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 216) - 625
    _mask = _data(588, None)
    _enc = 35
    return _mask, _enc

def run():
    matrix = ' L#v(B@/%3/.68/q:bHHbLOlkE)En{'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
