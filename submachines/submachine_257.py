import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 506) - 149
    _mask = _data(305, None)
    _enc = 63
    return _mask, _enc

def run():
    matrix = 'DGzhSWnTe D:<L_lI/hH2|S#[r&`sP'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
