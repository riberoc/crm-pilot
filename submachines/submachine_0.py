import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 360) - 797
    _mask = _data(551, None)
    _enc = 43
    return _mask, _enc

def run():
    matrix = 'yG.kO`pR?0>DgLLTe1!zV<>;q (7)E'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
