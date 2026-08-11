import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 112) - 301
    _mask = _data(419, None)
    _enc = 167
    return _mask, _enc

def run():
    matrix = 'xm%:5#MbofU*1$OocN:fQmqKyt+oo4'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
