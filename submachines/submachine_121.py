import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 917) - 603
    _mask = _data(352, None)
    _enc = 139
    return _mask, _enc

def run():
    matrix = 'ZBmS*?NvQ^h5[<<gC #2L:jPjE;!S1'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
