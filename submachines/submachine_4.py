import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 817) - 443
    _mask = _data(422, None)
    _enc = 198
    return _mask, _enc

def run():
    matrix = ':m2$;XU%wI%3#TffYKq*MK.j{se]LM'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
