import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 637) - 460
    _mask = _data(21, None)
    _enc = 136
    return _mask, _enc

def run():
    matrix = 'oLGj.OuHBI!>5HlP5<#i O0#;)cY3~'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
