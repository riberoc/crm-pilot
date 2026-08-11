import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 969) - 241
    _mask = _data(657, None)
    _enc = 105
    return _mask, _enc

def run():
    matrix = 'GvP(xE,U_x_orB 9l`=*B^[f)/<{65'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
