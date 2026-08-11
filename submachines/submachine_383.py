import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 423) - 842
    _mask = _data(581, None)
    _enc = 130
    return _mask, _enc

def run():
    matrix = '|3=O:c,>lF<6H!jIZ-wofD[~3W Yu7'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
