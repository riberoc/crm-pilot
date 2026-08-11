import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 780) - 337
    _mask = _data(633, None)
    _enc = 40
    return _mask, _enc

def run():
    matrix = 'EN+<&L5$(Jp1 mIC<aD(mhhCnPte*e'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
