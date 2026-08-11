import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 967) - 383
    _mask = _data(562, None)
    _enc = 98
    return _mask, _enc

def run():
    matrix = 'b.([SjTi;FQ%o6:rK}Tg o;0C{F4@U'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
