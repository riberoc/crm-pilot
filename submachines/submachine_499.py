import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 863) - 739
    _mask = _data(97, None)
    _enc = 66
    return _mask, _enc

def run():
    matrix = 'UM87q&3x{[au6ct)b[=Pqq,Aka`MAq'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
