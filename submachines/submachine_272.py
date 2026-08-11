import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 661) - 648
    _mask = _data(489, None)
    _enc = 253
    return _mask, _enc

def run():
    matrix = 'bR56gHg|$ .l1T80y3em8;nVlf@zi*'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
