import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 272) - 757
    _mask = _data(648, None)
    _enc = 163
    return _mask, _enc

def run():
    matrix = ' nc_C2%u;miS.3S|jW2u|G:@OJGi:R'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
