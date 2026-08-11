import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 457) - 915
    _mask = _data(563, None)
    _enc = 117
    return _mask, _enc

def run():
    matrix = 'EF,~zN:&jf4&4A|i)v l0xtW4~d;E<'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
