import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 837) - 353
    _mask = _data(346, None)
    _enc = 190
    return _mask, _enc

def run():
    matrix = ' 26Ffy6rqY-N]OI=dD{5Q/BlHTpE4{'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
