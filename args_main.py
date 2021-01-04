import argparse
import datetime


parser = argparse.ArgumentParser(description='Searches  for invalid pixels in NC files.')
parser.add_argument('satellite', choices=['16', '17', '18', 'g16', 'g17', 'g18', 'G16', 'G17', 'G18'], type=str, nargs='?')
parser.add_argument('input2', nargs='?', help='optional test')
parser.add_argument('--output_csv', nargs='?', const='this is optional', help='optional test')

print(parser.parse_args(['--output_csv', 'ME!!!', '--output_csv', 'test?']))
print(parser.parse_args(['--output_csv']))
print(parser.parse_args([]))
print(parser.parse_args(['g17']))