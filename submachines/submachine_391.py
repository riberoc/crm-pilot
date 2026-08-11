import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 886) - 808
    _mask = _data(26, None)
    _enc = 69
    return _mask, _enc

def run():
    matrix = '@tLS^UPs)~[_U-6Vo%nqP>qbu((od8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
