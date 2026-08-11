import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 233) - 912
    _mask = _data(858, None)
    _enc = 52
    return _mask, _enc

def run():
    matrix = 'KBi(J/xsr&2/Zdg`=!}w@fJ K`V@XI'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
