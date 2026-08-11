import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 366) - 438
    _mask = _data(138, None)
    _enc = 47
    return _mask, _enc

def run():
    matrix = 'D !^]z89HHFN`_}|6&Gu1Ex{5?zJos'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
