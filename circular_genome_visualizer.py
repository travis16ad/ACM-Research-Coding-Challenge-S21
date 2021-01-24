from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio import SeqIO
from Bio.Graphics import GenomeDiagram

def main():
    input_file = 'Genome.gb' # make this not hardcoded later
    output_file = 'gen.png' # make this not hardcoded later
    # input time
    with open(input_file) as infile:
        gb_rec = SeqIO.read(infile, 'genbank')
        # print(gb_rec._seq)
        print(dir(GenomeDiagram.Diagram))
        diagram = GenomeDiagram.Diagram(name='test')
        feature_track = diagram.new_track(1, name='test track')
        feature_set = feature_track.new_set()
        for feature in gb_rec.features:
            if feature.type != 'gene':
                print(feature)
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
                end=len(gb_rec),
                circle_core=0.7,
        )
        diagram.write(output_file, 'PNG')


if __name__ == '__main__':
    main()
