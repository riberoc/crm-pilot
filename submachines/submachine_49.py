import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 475) - 490
    _mask = _data(974, None)
    _enc = 45
    return _mask, _enc

def run():
    matrix = '#oZ^|` o3g7l0T$<Zw[!uTkw.$Wl^['
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
