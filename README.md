# Use
## Dependencies (pip)
* reportlab
* biopython

## Instructions
    python circular_genome_visualizer.py -h

# The process
## Stage One - Parsing and Recording
When I started out, I knew the two halves of this task would be going from text to data usable by my visualizer and going from that data to an image.
Once I researched "Genbank Python", I quickly found Biopython.

## Stage Two - Visualizing
There were easy to find visualization tools for Python, but it was harder to find Circos, that does specifically circles.
I found Circos when I found Circular-genome-visualizer, an entire project that was similar to what you wanted us to implement, which I found by searching "Python Genbank visualize" (this is no longer in my sources because I ended up using no code from it).
After more research, I realized that Circos was unecessary, as I could do everything in Biopython, just as their tutorial PDF showed.

# Sources
1. Genbank
 1. [Biopython](https://biopython.org)
1. Tutorials
 1. [Biopython tutorial.pdf](http://biopython.org/DIST/docs/tutorial/Tutorial.pdf)
1. Other features
 1. [Argument parsing](https://docs.python.org/3/howto/argparse.html)
