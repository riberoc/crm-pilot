import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 345) - 193
    _mask = _data(209, None)
    _enc = 201
    return _mask, _enc

def run():
    matrix = 'Gc8d41,qFTmoHo y.-Qp*C,HBwz,V~'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
