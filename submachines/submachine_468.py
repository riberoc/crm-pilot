import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 861) - 713
    _mask = _data(443, None)
    _enc = 7
    return _mask, _enc

def run():
    matrix = 'HCt0+3!Jp|xOF6jt+6i!l`KJ]C ?56'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
