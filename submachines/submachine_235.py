import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 605) - 574
    _mask = _data(184, None)
    _enc = 182
    return _mask, _enc

def run():
    matrix = '6RP,.<H&rDl1e@I]CcV;TqTEbK-^ek'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
