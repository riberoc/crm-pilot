import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 492) - 224
    _mask = _data(98, None)
    _enc = 164
    return _mask, _enc

def run():
    matrix = 'x4@3m9(p-h j]Tf()D!EI$#Fp1DBd5'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
