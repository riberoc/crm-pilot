import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 493) - 235
    _mask = _data(75, None)
    _enc = 184
    return _mask, _enc

def run():
    matrix = 'km4 ;rsx2wG*S9M319^j*n-qcyk`/+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
