import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 470) - 666
    _mask = _data(657, None)
    _enc = 181
    return _mask, _enc

def run():
    matrix = 'NmC.~,_1Q,plEx+P#xM;zl1C aCk5T'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
