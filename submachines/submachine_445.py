import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 129) - 730
    _mask = _data(797, None)
    _enc = 210
    return _mask, _enc

def run():
    matrix = '?AMS0JSOyoF?^m4+ nU)&~hY5y_M19'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
