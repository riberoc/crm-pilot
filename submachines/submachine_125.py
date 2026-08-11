import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 536) - 793
    _mask = _data(457, None)
    _enc = 165
    return _mask, _enc

def run():
    matrix = 'SlCoICmV<U!`Jqv}]`8^1.WI-gN/R '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
