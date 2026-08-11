import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 830) - 125
    _mask = _data(639, None)
    _enc = 197
    return _mask, _enc

def run():
    matrix = '0 0[v/aMjScUnOsdo8RZq~LXvA%~T]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
