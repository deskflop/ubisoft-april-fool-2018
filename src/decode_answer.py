#!/usr/bin/env python3 or #!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys


def main():
    note = [40, 5, 17, 1, 27, 4, 7, 8, 26, 9, 10, 11, 42, 35, 12, 2, 13, 15, 16, 19, 20, 21, 22, 18, 23, 24, 25, 6, 28,
            29, 30, 31, 32, 3, 33, 34, 36, 37, 38, 39, 14, 41, 43, 44]
    voice = list('wyTHwppreilFreoaos!pe"ayf-rAard"tpogtarelad.')
    answer = len(voice)*[None]
    for i, n in enumerate(note):
        answer[n-1] = voice[i]
    print(''.join(answer))  # output: HappyAprilFools!Type"af-reward"togetareward.
    return 0


if __name__ == "__main__":
    sys.exit(main())
