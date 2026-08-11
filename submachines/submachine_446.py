import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 513) - 265
    _mask = _data(1005, None)
    _enc = 237
    return _mask, _enc

def run():
    matrix = '{AqT6o^*8JPiC~ pdl6W=wSs]ELUmi'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
