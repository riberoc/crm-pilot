import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 533) - 695
    _mask = _data(249, None)
    _enc = 44
    return _mask, _enc

def run():
    matrix = 'ucY4FwIn#jF.!;Ss#~:XJ,zjp %==Q'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
