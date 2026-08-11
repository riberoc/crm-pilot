import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 526) - 917
    _mask = _data(508, None)
    _enc = 86
    return _mask, _enc

def run():
    matrix = 'd#@TVL;~rdX $+2E]E#!3SO.zjHFdM'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
