import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 292) - 210
    _mask = _data(98, None)
    _enc = 100
    return _mask, _enc

def run():
    matrix = 'JL78(Kxkc2^%E(1i MgY*6G?2%<(nF'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
