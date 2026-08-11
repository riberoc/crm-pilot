import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 466) - 376
    _mask = _data(999, None)
    _enc = 172
    return _mask, _enc

def run():
    matrix = '_1~F1sVS~}?*=lj8[ dA8;eozFx@Zh'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
