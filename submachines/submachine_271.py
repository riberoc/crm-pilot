import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 991) - 864
    _mask = _data(69, None)
    _enc = 38
    return _mask, _enc

def run():
    matrix = ';%6s:2k>(gn3<SYoqu4IJ.H9&xXth}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
