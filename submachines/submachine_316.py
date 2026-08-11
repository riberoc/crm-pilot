import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 898) - 614
    _mask = _data(309, None)
    _enc = 72
    return _mask, _enc

def run():
    matrix = '~n*N-HtdO<gE!!cP<gqAVr`c6 2@E9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
