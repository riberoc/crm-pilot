import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 949) - 940
    _mask = _data(1847, None)
    _enc = 203
    return _mask, _enc

def run():
    matrix = 'UyIsduQBQh[S>VFup1T@CFmxa}B_) '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
