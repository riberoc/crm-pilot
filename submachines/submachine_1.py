import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 858) - 629
    _mask = _data(81, None)
    _enc = 148
    return _mask, _enc

def run():
    matrix = 'dz 3[.;Ll}ZhXgi(O2kn-V=W,XI#W?'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
