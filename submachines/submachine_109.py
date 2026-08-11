import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 659) - 975
    _mask = _data(1772, None)
    _enc = 182
    return _mask, _enc

def run():
    matrix = 'mFodfw cuLWF6CpjuosCM$|8u~##SO'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
