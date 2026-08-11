import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 664) - 901
    _mask = _data(1717, None)
    _enc = 162
    return _mask, _enc

def run():
    matrix = '3*h.zJL,AfeGAsAk%mg>y)05%3)LLQ'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
