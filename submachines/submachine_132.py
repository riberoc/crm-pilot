import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 465) - 928
    _mask = _data(1477, None)
    _enc = 123
    return _mask, _enc

def run():
    matrix = 'A<^,Ac1Vp7NQ.]QTWNx_[G:,G1bB=r'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
