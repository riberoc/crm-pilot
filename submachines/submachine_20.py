import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 764) - 482
    _mask = _data(193, None)
    _enc = 73
    return _mask, _enc

def run():
    matrix = 'Fe+EBj7h(bb,Yxgy9XtN?5:kM2vZ&c'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
