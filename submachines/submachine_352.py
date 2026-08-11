import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 518) - 374
    _mask = _data(62, None)
    _enc = 216
    return _mask, _enc

def run():
    matrix = '}(PW87*f&S{5jbEh^0t7zi<!YR Xv9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
