import cvx_codes
import os
import sys


def main():

    db_path = sys.argv[1]

    if not os.path.exists(os.path.dirname(db_path)):
        abs_path = os.path.abspath(db_path)
        print '>>> Attempting to create new database: ' + abs_path
        print '>>> Folder %s does not exist' % os.path.dirname(abs_path)
        print '>>> Please create it.'
        sys.exit(1)

    process = sys.argv[2]

    if process == 'cvx':
        cvx_codes.main(db_path)
    else:
        print 'choose which data to import  [cvx]'


if __name__ == '__main__':
    main()
