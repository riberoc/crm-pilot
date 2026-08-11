import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 305) - 178
    _mask = _data(161, None)
    _enc = 217
    return _mask, _enc

def run():
    matrix = 'Ju9u{C; sfGG]~axOVU1dxfzOK}A5W'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
