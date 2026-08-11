import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 272) - 936
    _mask = _data(737, None)
    _enc = 83
    return _mask, _enc

def run():
    matrix = '7X9cMd&_buNQF_@ACudIkUk2CW ~y3'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
