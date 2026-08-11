import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 730) - 109
    _mask = _data(960, None)
    _enc = 163
    return _mask, _enc

def run():
    matrix = 'Tl;&C*VQsa/Md| Be<Eu20#$>A71pB'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
