import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 521) - 523
    _mask = _data(48, None)
    _enc = 46
    return _mask, _enc

def run():
    matrix = 'anz=NB$MCBUW1tmX}F{l>d)]blPI+9'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
