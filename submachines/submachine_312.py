import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 248) - 607
    _mask = _data(543, None)
    _enc = 153
    return _mask, _enc

def run():
    matrix = 'v_CbX,&70]@PawOpQ @C_JBEW[sKk*'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
