import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 310) - 484
    _mask = _data(783, None)
    _enc = 88
    return _mask, _enc

def run():
    matrix = '/kxnrTVA8g4$6 i6P=e0_%#gdKY~4b'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
