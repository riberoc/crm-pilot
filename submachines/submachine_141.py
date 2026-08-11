import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 226) - 622
    _mask = _data(565, None)
    _enc = 106
    return _mask, _enc

def run():
    matrix = '*?h l=M,L*bZfF:)t(ebpwDj7dMrMZ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
