import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 569) - 354
    _mask = _data(32, None)
    _enc = 181
    return _mask, _enc

def run():
    matrix = 'ef 9$OR4CT#`q-V0@2x~~6t9<76|Za'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
