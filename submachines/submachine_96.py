import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 330) - 773
    _mask = _data(613, None)
    _enc = 40
    return _mask, _enc

def run():
    matrix = 'Q3 D+#K#mm[QS(JLvE<mSkcRFVb~KW'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
