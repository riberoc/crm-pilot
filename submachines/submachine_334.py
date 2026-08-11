import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 149) - 499
    _mask = _data(543, None)
    _enc = 135
    return _mask, _enc

def run():
    matrix = '[0F_NTf{*&LLt-<s _{T9.Z0mS4gm?'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
