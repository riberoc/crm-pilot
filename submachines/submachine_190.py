import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 881) - 554
    _mask = _data(106, None)
    _enc = 250
    return _mask, _enc

def run():
    matrix = 'YmMTXXaBk.; <9}vzDE:<<5^)9kju5'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
