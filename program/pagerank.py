import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are a list of all other pages in the corpus that are linked to by the page.
    """
    raise NotImplementedError


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next, given a current page.
    With probability `damping_factor`, choose a link at random linked to by `page`. With probability `1 - damping_factor`, choose a link at random chosen from all pages in the corpus.
    """
    raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages according to transition model, starting with a page at random.
    Return a dictionary where keys are page names, and values are their estimated PageRank value (a value between 0 and 1). All PageRank values should sum to 1.
    """
    raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating PageRank values until convergence.
    Return a dictionary where keys are page names, and values are their estimated PageRank value (a value between 0 and 1). All PageRank values should sum to 1.
    """
    raise NotImplementedError


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")

    corpus = crawl(sys.argv[1])

    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")    

    print(f"PageRank Results from Iteration")
    ranks = iterate_pagerank(corpus, DAMPING)
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")   