import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 741) - 577
    _mask = _data(488, None)
    _enc = 207
    return _mask, _enc

def run():
    matrix = 'L*%tiK,.3K)~=woj})N4rW,-vw1NK>'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
