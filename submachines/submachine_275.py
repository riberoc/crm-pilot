import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 614) - 554
    _mask = _data(365, None)
    _enc = 241
    return _mask, _enc

def run():
    matrix = 'c~[ep2A$t~Py,xhb hL;5trT;@NfP['
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
