import sys
import unittest
import pangrams
import contextlib
from io import StringIO


@contextlib.contextmanager
def capture(stream_name):
    orig_stream = getattr(sys, stream_name)
    setattr(sys, stream_name, StringIO())
    try:
        yield getattr(sys, stream_name)
    finally:
        setattr(sys, stream_name, orig_stream)

def stdout():
    return capture('stdout')

@contextlib.contextmanager
def stdin(input_=None):
    with capture('stdin') as stdin:
        if input_:
            stdin.write(input_)
            stdin.seek(0)
            yield stdin


class PangramTest(unittest.TestCase):

    def check_pang_main(self, inp, expected_out):
        with stdin(inp), stdout() as out:
            pangrams.main()
            self.assertEqual(out.getvalue(), expected_out)

    def test_pangram(self):
        inp = ('1\n'
               'The quick brown fox jumps over the lazy dog.\n')
        out = ('True a: 1, b: 1, c: 1, d: 1, e: 3, f: 1, g: 1, h: 2, i: 1, '
               'j: 1, k: 1, l: 1, m: 1, n: 1, o: 4, p: 1, q: 1, r: 2, s: 1, '
               't: 2, u: 2, v: 1, w: 1, x: 1, y: 1, z: 1\n')
        self.check_pang_main(inp, out)

    def test_not_pangram(self):
        inp = ('1\n'
               'A\n')
        out = 'False a: 1\n'
        self.check_pang_main(inp, out)

    def test_multiple_inputs(self):
        inp = ('3\n'
               'The quick brown fox jumps over the lazy dog.\n'
               'Pack my box with five dozen liquor jugs\n'
               'Saxophones quickly blew over my jazzy hair\n')
        out = ('True a: 1, b: 1, c: 1, d: 1, e: 3, f: 1, g: 1, h: 2, i: 1, '
               'j: 1, k: 1, l: 1, m: 1, n: 1, o: 4, p: 1, q: 1, r: 2, s: 1, '
               't: 2, u: 2, v: 1, w: 1, x: 1, y: 1, z: 1\n'

               'True a: 1, b: 1, c: 1, d: 1, e: 2, f: 1, g: 1, h: 1, i: 3, '
               'j: 1, k: 1, l: 1, m: 1, n: 1, o: 3, p: 1, q: 1, r: 1, s: 1, '
               't: 1, u: 2, v: 1, w: 1, x: 1, y: 1, z: 1\n'

               'False a: 3, b: 1, c: 1, e: 3, h: 2, i: 2, j: 1, k: 1, l: 2, '
               'm: 1, n: 1, o: 3, p: 1, q: 1, r: 2, s: 2, u: 1, v: 1, w: 1, '
               'x: 1, y: 3, z: 2\n')
        self.check_pang_main(inp, out)

if __name__ == '__main__':
    unittest.main()
