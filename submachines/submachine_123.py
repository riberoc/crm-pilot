import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 450) - 931
    _mask = _data(1482, None)
    _enc = 127
    return _mask, _enc

def run():
    matrix = '^@+d?bUAH1Iazwy{Yh5u!OazO, lnF'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
