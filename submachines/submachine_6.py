import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 478) - 230
    _mask = _data(21, None)
    _enc = 237
    return _mask, _enc

def run():
    matrix = 'f~b%lx&: d,F%!`M(fiWvVA(ucXM>s'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
