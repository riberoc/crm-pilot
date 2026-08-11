import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 512) - 233
    _mask = _data(779, None)
    _enc = 50
    return _mask, _enc

def run():
    matrix = 'IeN^vL827>eNUg$v Hx|ue:TXF|Idh'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
