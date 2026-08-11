import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 791) - 568
    _mask = _data(452, None)
    _enc = 145
    return _mask, _enc

def run():
    matrix = 'FV8.aL`,PA 25HNV|Zp3M^q(>>C~$_'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
