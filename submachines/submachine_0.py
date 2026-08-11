import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 316) - 195
    _mask = _data(129, None)
    _enc = 226
    return _mask, _enc

def run():
    matrix = '4Lg_LU+O?TzMU^QjemN,$l&U 36Tj]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
