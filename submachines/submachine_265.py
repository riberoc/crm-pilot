import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 300) - 974
    _mask = _data(1367, None)
    _enc = 186
    return _mask, _enc

def run():
    matrix = 'ax^kKc3A_N!9XPc!`p0?0GJ %njY5X'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
