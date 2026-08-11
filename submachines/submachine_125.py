import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 863) - 460
    _mask = _data(274, None)
    _enc = 136
    return _mask, _enc

def run():
    matrix = 'HB;|M,>D$ <b>#:q|4[{mE<6x.d9{9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
