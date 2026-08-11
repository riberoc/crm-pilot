import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 366) - 664
    _mask = _data(589, None)
    _enc = 142
    return _mask, _enc

def run():
    matrix = 'L)pB! .E3LT,;VPTF5=sHu~grDMG)X'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
