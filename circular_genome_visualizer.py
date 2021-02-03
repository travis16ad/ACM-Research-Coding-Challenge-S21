from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio import SeqIO
from Bio.Graphics import GenomeDiagram
import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='properly formatted Genbank file')
    parser.add_argument('output_file', help='name of ouput PNG')
    args = parser.parse_args()
    if not args.output_file.lower().endswith('.png'):
        print('Output file must be png')
        sys.exit(1)
    return (args.input_file, args.output_file)

def read_genbank(input_file):
    with open(input_file) as infile:
        return SeqIO.read(infile, 'genbank')

def make_diagram(genbank_record, output_file):
    diagram = GenomeDiagram.Diagram(name='test')
    feature_track = diagram.new_track(1, name='test track')
    feature_set = feature_track.new_set()
    for feature in genbank_record.features:
        if feature.type != 'gene':
            continue
        if len(feature_set) % 2 == 0:
            color = colors.blue
        else:
            color = colors.lightblue
        feature_set.add_feature(feature, color=color, label=True)
    diagram.draw(
            format='circular',
            circular=True,
            pagesize=(20 * cm, 20 * cm),
            start=0,
            end=len(genbank_record),
            circle_core=0.7,
    )
    diagram.write(output_file, 'PNG')

def main():
    input_file, output_file = parse_arguments()
    gb_rec = read_genbank(input_file)
    make_diagram(gb_rec, output_file)

if __name__ == '__main__':
    main()
