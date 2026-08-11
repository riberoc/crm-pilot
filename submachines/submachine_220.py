import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 894) - 614
    _mask = _data(390, None)
    _enc = 129
    return _mask, _enc

def run():
    matrix = '=.hIC[:cve[81XNr%3.eL1iD21g?:]'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
