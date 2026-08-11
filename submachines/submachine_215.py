import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 793) - 392
    _mask = _data(702, None)
    _enc = 23
    return _mask, _enc

def run():
    matrix = '+ox7b0Bq #fRi#mZEq5tbe$mThC8c}'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
