import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 505) - 919
    _mask = _data(587, None)
    _enc = 25
    return _mask, _enc

def run():
    matrix = 'Zp vP~D+Y:u{u+Z7PjLloag=urx3^o'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
