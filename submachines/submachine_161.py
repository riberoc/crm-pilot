import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 132) - 826
    _mask = _data(970, None)
    _enc = 29
    return _mask, _enc

def run():
    matrix = ':C,{D+u`q %w/:YZnh;ZIEar[3lI{;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
