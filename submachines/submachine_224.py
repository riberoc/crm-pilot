import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 133) - 311
    _mask = _data(349, None)
    _enc = 180
    return _mask, _enc

def run():
    matrix = 'kB5^.mq[Fgt*,ypIJ[hMA 2t_qzO*q'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
