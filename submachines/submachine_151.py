import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 568) - 481
    _mask = _data(101, None)
    _enc = 106
    return _mask, _enc

def run():
    matrix = '#~}D@3Xd;,nnzocSI|tbIs ?7yD_av'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
