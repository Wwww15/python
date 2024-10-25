import argparse

parser = argparse.ArgumentParser(prog='test_args_parse', description='This is a test args parse program.',
                                 epilog='2024-10-13 end.')

parser.add_argument("--user", required=True)
parser.add_argument("--pwd", required=True)
parser.add_argument("--addr", required=True)
parser.add_argument("--port", required=True)
parser.add_argument("fileaddr")

args = parser.parse_args()
for k, v in vars(args).items():
    print(k + ':' + v)
