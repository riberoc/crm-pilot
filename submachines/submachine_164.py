import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 456) - 200
    _mask = _data(210, None)
    _enc = 92
    return _mask, _enc

def run():
    matrix = '_=bo+y7t#eGZ02 yx+[HLfk65bQhYQ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
