import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 782) - 538
    _mask = _data(395, None)
    _enc = 96
    return _mask, _enc

def run():
    matrix = 'S>s%+t5],>Y egq(wL/Nf8kMN2FNJT'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
