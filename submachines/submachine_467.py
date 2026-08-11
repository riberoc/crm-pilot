import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 169) - 370
    _mask = _data(267, None)
    _enc = 57
    return _mask, _enc

def run():
    matrix = 'Oq@LN[FQ_ Z&?@]u?vigim9`L}54j['
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
