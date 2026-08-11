import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 228) - 213
    _mask = _data(415, None)
    _enc = 164
    return _mask, _enc

def run():
    matrix = '4R ndn:{&$T>|_d4)sp!ZMvYB`,$8,'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
