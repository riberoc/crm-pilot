import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 149) - 610
    _mask = _data(625, None)
    _enc = 140
    return _mask, _enc

def run():
    matrix = 'fq6wrNA}V7SL,G C8KZL8s@.!EL,]r'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
