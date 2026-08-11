import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 904) - 575
    _mask = _data(187, None)
    _enc = 242
    return _mask, _enc

def run():
    matrix = 'k6[BPx Sa~80)f&Bi@<Mu]jvFRh0O@'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
