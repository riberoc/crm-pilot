import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 724) - 778
    _mask = _data(276, None)
    _enc = 186
    return _mask, _enc

def run():
    matrix = '*d%9.jd]Z&3s 76Jd0Im?RHb4W71Vx'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
