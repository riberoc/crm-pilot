import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 464) - 251
    _mask = _data(123, None)
    _enc = 162
    return _mask, _enc

def run():
    matrix = '4az8$5=G;L7lF?o+S^ dYNmbb&7,H6'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
