import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 761) - 770
    _mask = _data(415, None)
    _enc = 99
    return _mask, _enc

def run():
    matrix = 'kQuctgC fh>9j}hc+Sd#h4m6s9_:vp'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
