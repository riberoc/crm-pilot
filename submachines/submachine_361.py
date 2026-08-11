import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 557) - 831
    _mask = _data(408, None)
    _enc = 116
    return _mask, _enc

def run():
    matrix = 'PGXdya*Fqy{pnXT7E>dq>lJV|C`NI>'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
