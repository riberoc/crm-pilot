import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 778) - 558
    _mask = _data(402, None)
    _enc = 104
    return _mask, _enc

def run():
    matrix = 'ZO geGtsooJ]QO^`M05_sbhj.r;y^P'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
