import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 123) - 486
    _mask = _data(389, None)
    _enc = 5
    return _mask, _enc

def run():
    matrix = '*8Q_frBu((J<z}y-+0?=<?ZL4B7kY '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
