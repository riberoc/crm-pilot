import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 612) - 348
    _mask = _data(109, None)
    _enc = 163
    return _mask, _enc

def run():
    matrix = 'VH+9T/)3<MyHUz 3iCiw,:=7GRHCxF'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
