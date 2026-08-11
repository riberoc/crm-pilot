import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 843) - 299
    _mask = _data(703, None)
    _enc = 197
    return _mask, _enc

def run():
    matrix = 'bVo#=s0|327& {AQ{A=WdbFcuW?&$_'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
