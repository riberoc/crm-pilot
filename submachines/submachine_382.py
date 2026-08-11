import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 368) - 310
    _mask = _data(175, None)
    _enc = 187
    return _mask, _enc

def run():
    matrix = 'Q<6M2$0#`3vvwO8(oKein,qiDVTb*F'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
