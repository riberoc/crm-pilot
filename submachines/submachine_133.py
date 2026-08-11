import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 194) - 597
    _mask = _data(552, None)
    _enc = 130
    return _mask, _enc

def run():
    matrix = '7$ru!AB/4<^H4_qO2}UQxu$soHiqp>'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
