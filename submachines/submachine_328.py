import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 752) - 454
    _mask = _data(160, None)
    _enc = 130
    return _mask, _enc

def run():
    matrix = 'Ti?W(6]vlagF[xo?dAZ*j^^Vwn~oB+'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
