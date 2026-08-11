import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 740) - 241
    _mask = _data(980, None)
    _enc = 47
    return _mask, _enc

def run():
    matrix = '|16J=}3lu<<ku+QNeQ+Z!Kbqnu#jR['
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
