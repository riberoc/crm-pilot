import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 798) - 618
    _mask = _data(446, None)
    _enc = 38
    return _mask, _enc

def run():
    matrix = '^gq.?CZ9nB}q3BfC );iQ=/?8t?_TM'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
