import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 879) - 220
    _mask = _data(747, None)
    _enc = 189
    return _mask, _enc

def run():
    matrix = 'eNgX*OBn@[;@v9&R&9yO7 o=&hPHpT'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
