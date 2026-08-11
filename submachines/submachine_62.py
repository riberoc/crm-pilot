import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 910) - 811
    _mask = _data(247, None)
    _enc = 83
    return _mask, _enc

def run():
    matrix = 'K0s}(M{=<%>?&RXfI]0}%x,,e?&k$T'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
