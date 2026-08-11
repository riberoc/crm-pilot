import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 399) - 879
    _mask = _data(533, None)
    _enc = 38
    return _mask, _enc

def run():
    matrix = 'A7`kbvm7/VL?lt;E5#-q%O0xHrciC;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
