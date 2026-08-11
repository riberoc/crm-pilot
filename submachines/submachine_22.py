import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 840) - 632
    _mask = _data(470, None)
    _enc = 49
    return _mask, _enc

def run():
    matrix = '$qNYCAZx=VhqZJ[/})7=/|4 @lK;wI'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
