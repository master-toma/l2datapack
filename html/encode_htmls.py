import os
import sys
import codecs
import argparse

def read_to_utf16(file_path):
    with open(file_path, "rb") as infile:
        data = infile.read()
        # encode without BOM
        return data.decode('utf-8').encode('utf-16le')

def read_to_utf8(file_path):
    with open(file_path, "rb") as infile:
        data = infile.read()
        # encode without BOM
        return data.decode('utf-16').encode('utf-8')

parser = argparse.ArgumentParser(description='Optional app description')

parser.add_argument('-e', dest='extension', default=".htm")
parser.add_argument('--root_dir', dest='root_dir', default='./')
parser.add_argument('--out_dir', dest='out_dir', default='./')
parser.add_argument('--to_utf8', dest='to_utf8', default='0')

parser.set_defaults(join_lines=False)

args = parser.parse_args()

to_utf8 = args.to_utf8 == '1'
root_dir = os.path.abspath(args.root_dir)
out_dir =  os.path.abspath(args.out_dir)

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        pass

file_count = 0;

print "Enconding from '%s' to '%s'..." %(root_dir, out_dir)

for root, subdirs, files in os.walk(root_dir):
    for filename in files:
        file_path = os.path.join(root, filename)
        if not file_path.endswith(args.extension):
            continue;

        if to_utf8:
            content = read_to_utf8(file_path)
        else:
            content = read_to_utf16(file_path)

        mkdir_p(out_dir)
        outfile = open(os.path.join(out_dir, filename), "w+b")
        if not to_utf8:
            newFileByteArray = bytearray(b'\xff\xfe')
            outfile.write(newFileByteArray)

        outfile.write(content)
        outfile.close()
        file_count +=  1
        if file_count % 1000 == 0:
            print "%d '*%s' files were encoded to %s..." %(file_count, args.extension, out_dir)

print "%d '*%s' files were encoded to %s... Done" %(file_count, args.extension, out_dir)


