import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 470) - 377
    _mask = _data(78, None)
    _enc = 7
    return _mask, _enc

def run():
    matrix = 'FF#h827>,7c~#v}m8u(;j5O# +f=.O'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
