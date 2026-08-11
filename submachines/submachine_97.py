import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 685) - 623
    _mask = _data(21, None)
    _enc = 74
    return _mask, _enc

def run():
    matrix = 'Gsg MpS.ol4@oR(x4XHu7GgH2%@KWq'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
