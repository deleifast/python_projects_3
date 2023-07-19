import sys

def main(argv):
    if len(argv) < 2:
        sys.stderr.write("Usage: %s <database>" % (argv[0],))
        return 1

    if not os.path.exists(argv[1]):
        sys.stderr.write("ERROR: Database %r was not found!" % (argv[1],))
        return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))