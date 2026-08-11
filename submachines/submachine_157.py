import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 810) - 148
    _mask = _data(519, None)
    _enc = 154
    return _mask, _enc

def run():
    matrix = 'mJphR{*w_kDj,c-x|jLh`EYN~|Nevl'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
