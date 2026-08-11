import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 440) - 158
    _mask = _data(253, None)
    _enc = 168
    return _mask, _enc

def run():
    matrix = 'pK;>wvz&g!y},@E <>|0NGC=S^:W-2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
