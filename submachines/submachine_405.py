import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 477) - 924
    _mask = _data(555, None)
    _enc = 83
    return _mask, _enc

def run():
    matrix = 'FhM@^~>fX -JlS#[)5J}B9Kp`&%T;3'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
