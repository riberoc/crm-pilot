import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 174) - 305
    _mask = _data(263, None)
    _enc = 107
    return _mask, _enc

def run():
    matrix = '^`ZzJ4E}?F~,@9BfEY3 (P:_5y=U(2'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
