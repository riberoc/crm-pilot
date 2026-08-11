import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 272) - 215
    _mask = _data(510, None)
    _enc = 19
    return _mask, _enc

def run():
    matrix = 'kPRL.1M./nJ7D#].5NE>Q7mI`76ReD'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
