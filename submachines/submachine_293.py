import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 336) - 751
    _mask = _data(715, None)
    _enc = 189
    return _mask, _enc

def run():
    matrix = 'atyN&y,#<T*r~z|m~ S8?VT&&*K:$]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
