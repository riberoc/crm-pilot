import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 215) - 791
    _mask = _data(823, None)
    _enc = 223
    return _mask, _enc

def run():
    matrix = 'o_mXGmtG(d$Kd]2;-+|&[. 3K!Jatw'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
