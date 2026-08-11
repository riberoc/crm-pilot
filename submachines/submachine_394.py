import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 907) - 533
    _mask = _data(432, None)
    _enc = 41
    return _mask, _enc

def run():
    matrix = '4$igYDWbqfQc7cA `BOiqJ`q0Ew}/M'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
