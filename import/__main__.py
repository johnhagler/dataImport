import cvx_codes
import os
import sys


def main():

    db_path = sys.argv[1]

    if not os.path.exists(db_path):
        abs_path = os.path.abspath(db_path)
        os.mkdir(os.path.dirname(abs_path))

    process = sys.argv[2]

    if process == 'cvx':
        cvx_codes.main(db_path)
    else:
        print 'no options'


if __name__ == '__main__':
    main()
