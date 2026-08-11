import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 506) - 657
    _mask = _data(734, None)
    _enc = 135
    return _mask, _enc

def run():
    matrix = 'hr=}Ri1H:Xs:Y*~l~:lR u_$|:bP9e'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
