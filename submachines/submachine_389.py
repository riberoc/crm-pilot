import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 438) - 311
    _mask = _data(78, None)
    _enc = 214
    return _mask, _enc

def run():
    matrix = 'uP]BA+?)1g|g(>|>d_8pHXAse`klx3'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
