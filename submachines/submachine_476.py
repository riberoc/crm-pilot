import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 244) - 990
    _mask = _data(1148, None)
    _enc = 171
    return _mask, _enc

def run():
    matrix = 'Z J%liR#$NtVy4DjFH%Q)|r<T=i!#P'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
