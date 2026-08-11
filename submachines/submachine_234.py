import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 720) - 352
    _mask = _data(807, None)
    _enc = 130
    return _mask, _enc

def run():
    matrix = '8OaKX;n1cqW~Rer*0>jncdTgn{qz(['
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
