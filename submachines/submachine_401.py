import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 576) - 875
    _mask = _data(1577, None)
    _enc = 242
    return _mask, _enc

def run():
    matrix = '|F.+BT[&q~Up a$8ph*>}_fM>/[ex!'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
