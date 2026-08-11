import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 999) - 894
    _mask = _data(1958, None)
    _enc = 223
    return _mask, _enc

def run():
    matrix = 'i[(h-N8Fc-f:4gS@6YLe;YE3(W<U A'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
