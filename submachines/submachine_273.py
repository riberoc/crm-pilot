import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 688) - 949
    _mask = _data(1762, None)
    _enc = 155
    return _mask, _enc

def run():
    matrix = '[mBp#u T2{L::Z(Y7,s@&d>n*8#J(G'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
