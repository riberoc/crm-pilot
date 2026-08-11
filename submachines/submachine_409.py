import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 588) - 459
    _mask = _data(236, None)
    _enc = 222
    return _mask, _enc

def run():
    matrix = 'VW0_bc.>sNh BI<p%AXnEP2ek^Jj^S'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
