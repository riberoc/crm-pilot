import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 702) - 313
    _mask = _data(136, None)
    _enc = 237
    return _mask, _enc

def run():
    matrix = 'xir+b(|ouX<xM5+U MwDd@9RA%L58W'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
