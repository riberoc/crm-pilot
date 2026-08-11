import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 139) - 575
    _mask = _data(930, None)
    _enc = 237
    return _mask, _enc

def run():
    matrix = '*KXM<;/E.7&,<#4&WssNVRP~H=NOKN'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
