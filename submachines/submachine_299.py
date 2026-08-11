import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 850) - 373
    _mask = _data(257, None)
    _enc = 202
    return _mask, _enc

def run():
    matrix = '7Olnc7.us<7D686r&vt# LC&dzAYz7'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
