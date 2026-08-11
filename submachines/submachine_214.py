import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 888) - 101
    _mask = _data(1016, None)
    _enc = 7
    return _mask, _enc

def run():
    matrix = 'eLTnBJI[%=f)>&0A8A9~Ml6^ya<W <'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
