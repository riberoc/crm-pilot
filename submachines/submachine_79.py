import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 426) - 879
    _mask = _data(725, None)
    _enc = 31
    return _mask, _enc

def run():
    matrix = 'w.?6I-fTG+^560m !PZ_BXQW5I`2nM'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
