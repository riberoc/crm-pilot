import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 862) - 743
    _mask = _data(227, None)
    _enc = 216
    return _mask, _enc

def run():
    matrix = 'W2nO?Ruvd&;Bi0 ;x5+nRs<l9EH?Oc'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
