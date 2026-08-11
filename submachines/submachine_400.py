import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 531) - 213
    _mask = _data(775, None)
    _enc = 46
    return _mask, _enc

def run():
    matrix = '}}E?mS?e0+Ls3m{}fa/8k{:U9H*q&U'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
