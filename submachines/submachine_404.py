import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 679) - 329
    _mask = _data(176, None)
    _enc = 207
    return _mask, _enc

def run():
    matrix = '| sPY6[8<7iu0i]>4=pD4*zEr7V8]s'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
