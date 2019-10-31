import os
import sys
import codecs
import argparse

def read_to_utf16(file_path, skip_encoding, join):
    with open(file_path, "rb") as infile:
        data = infile.read()
        data = data.replace("    ", "\t")
        if join:
            data = data.replace("\r\n", "\t")
            data = data.strip()
            data += "\r\n"
        if skip_encoding:
            return data;

        # encode without BOM
        return data.decode('utf-8').encode('utf-16le')

global_id = 1;
def get_id(line, id_column):
    global global_id;
    if id_column <= 0:
        global_id += 1
        return global_id;

    line = line.replace('\t\t', '\t')
    tokens = line.split('\t')
    return int(tokens[id_column - 1])

parser = argparse.ArgumentParser(description='Optional app description')

parser.add_argument('-e', dest='extension', default=".txt")
parser.add_argument('--utf16', dest='utf16', default=True)
parser.add_argument('--skip_encoding', dest='skip_encoding', default=False)
parser.add_argument('--out_name', dest='out_name', default='merged.txt')
parser.add_argument('--root_dir', dest='root_dir', default='./')
parser.add_argument('--single_file', dest='single_file', default='')
parser.add_argument('--join_lines', dest='join_lines', action='store_true')
parser.add_argument('--id_column', dest='id_column', default=-1)
parser.add_argument('--append', dest='append', default="0")

parser.set_defaults(join_lines=False)

args = parser.parse_args()

rootdir = args.root_dir
out_file_path =  args.out_name

content_lines = dict()

if args.single_file:
    content = read_to_utf16(args.single_file, args.skip_encoding, args.join_lines)
    content_lines[1] = content
else:
    for root, subdirs, files in os.walk(rootdir):
        for filename in files:
            file_path = os.path.join(root, filename)
            if not file_path.endswith(args.extension):
                continue;

            content_utf8 = read_to_utf16(file_path, True, args.join_lines)
            line_id = get_id(content_utf8, int(args.id_column))

            content = read_to_utf16(file_path, args.skip_encoding, args.join_lines)

            #if args.join_lines:
            #    content = content.replace("\r\n".encode('utf-16le'), "\t".encode('utf-16le'))

            content_lines[line_id]= content

if args.append == "1":
    outfile = open(os.path.join(rootdir, out_file_path), "ab")
else:
    outfile = open(os.path.join(rootdir, out_file_path), "w+b")
    newFileByteArray = bytearray(b'\xff\xfe')
    outfile.write(newFileByteArray)

for key, value in content_lines.iteritems():
    outfile.write(value)

outfile.close()

if args.append == "1":
    print "%d '*%s' files were encoded and merged to %s" %(len(content_lines), args.extension, out_file_path)
else:
    print "%d '*%s' files were encoded and added to %s" %(len(content_lines), args.extension, out_file_path)


