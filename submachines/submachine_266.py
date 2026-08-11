import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 438) - 767
    _mask = _data(516, None)
    _enc = 171
    return _mask, _enc

def run():
    matrix = 'joUohB@ty3$0C%,DHu1fu,(I 3t}Uf'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
