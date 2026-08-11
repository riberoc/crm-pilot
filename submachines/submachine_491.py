import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 817) - 148
    _mask = _data(917, None)
    _enc = 17
    return _mask, _enc

def run():
    matrix = 'D PcEer<in&:o+e+23Q/e#`2mXx`RV'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
