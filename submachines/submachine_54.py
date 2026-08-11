import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 198) - 536
    _mask = _data(750, None)
    _enc = 18
    return _mask, _enc

def run():
    matrix = 'a/ .$t2ds_{v!_*HVgZSxJx7i-|dK8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
