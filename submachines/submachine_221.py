import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 539) - 240
    _mask = _data(897, None)
    _enc = 191
    return _mask, _enc

def run():
    matrix = 'VQVT5k=5heKV,rh4o}@E- 0/vUkv.#'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
