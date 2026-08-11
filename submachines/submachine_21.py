import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 653) - 595
    _mask = _data(459, None)
    _enc = 254
    return _mask, _enc

def run():
    matrix = '_U8vZ>~&)0bQ#is1^x>E!JK9Xya#Wf'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
