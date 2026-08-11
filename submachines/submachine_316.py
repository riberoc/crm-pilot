import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 594) - 464
    _mask = _data(96, None)
    _enc = 127
    return _mask, _enc

def run():
    matrix = 'D<{~|5)@YUJBdT2G#Q9#hR9I5%?$Ms'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
