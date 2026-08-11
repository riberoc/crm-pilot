import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 272) - 360
    _mask = _data(833, None)
    _enc = 226
    return _mask, _enc

def run():
    matrix = '8ASQXz}cA}a uEI&0CP/zAKdxgmC04'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
