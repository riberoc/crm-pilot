import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 869) - 149
    _mask = _data(557, None)
    _enc = 180
    return _mask, _enc

def run():
    matrix = 'U:h6a|/ =Sc,-F[Bx,;B>Xcr]Fk`A9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
