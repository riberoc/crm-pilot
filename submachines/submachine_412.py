import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 651) - 211
    _mask = _data(814, None)
    _enc = 214
    return _mask, _enc

def run():
    matrix = 'qtc? =ZOZW&CPU+4Qwp>lV2`03%u6^'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
