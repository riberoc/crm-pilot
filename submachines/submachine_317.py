import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 481) - 407
    _mask = _data(996, None)
    _enc = 103
    return _mask, _enc

def run():
    matrix = 'VjCs71FCU K$oQyx@pf$ESB#-ESO$8'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
