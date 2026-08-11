import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 392) - 759
    _mask = _data(660, None)
    _enc = 48
    return _mask, _enc

def run():
    matrix = '{DpM5712g:T]7H%.j`ot< #T5,R5lK'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
