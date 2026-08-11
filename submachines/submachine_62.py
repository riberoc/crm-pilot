import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 503) - 490
    _mask = _data(826, None)
    _enc = 247
    return _mask, _enc

def run():
    matrix = 'TaVD~=|l@ZF.wo;qzYqc M~7M2NNU;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
