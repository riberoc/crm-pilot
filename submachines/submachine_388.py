import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 770) - 741
    _mask = _data(52, None)
    _enc = 93
    return _mask, _enc

def run():
    matrix = 'YfsX$cLXo]kaiciS6EG~Z>YNKz.Swx'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
