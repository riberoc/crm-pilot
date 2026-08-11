import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 763) - 358
    _mask = _data(204, None)
    _enc = 196
    return _mask, _enc

def run():
    matrix = '@{&Eh^{#4>N@1bs$}a).# W}d&Wzq+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
