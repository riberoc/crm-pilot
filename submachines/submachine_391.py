import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 788) - 388
    _mask = _data(764, None)
    _enc = 124
    return _mask, _enc

def run():
    matrix = 'D+0Ei^3TR}X>];.>Y(&J${*c #&+P)'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
