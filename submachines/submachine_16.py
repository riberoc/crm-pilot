import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 582) - 497
    _mask = _data(37, None)
    _enc = 105
    return _mask, _enc

def run():
    matrix = 'cb{|v>`A6L$%>DY!<$|*2/ach4r Ri'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
