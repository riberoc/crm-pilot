import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 696) - 777
    _mask = _data(372, None)
    _enc = 213
    return _mask, _enc

def run():
    matrix = '%Ltp.{WH0&m?/p%11!Hv%s P0D^wCz'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
