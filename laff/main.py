import parasail


def parse_fasta(path):
    seqs = []
    cur = []
    with open(path, "r") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            if line.startswith(">"):
                if cur:
                    seqs.append("".join(cur))
                    cur = []
            else:
                cur.append(line)
    if cur:
        seqs.append("".join(cur))
    return seqs


def main():
    s, t = parse_fasta("rosalind_laff.txt")
    result = parasail.sw_trace_striped_16(s, t, 11, 1, parasail.blosum62)

    s_sub = s[result.cigar.beg_query : result.end_query + 1]
    t_sub = t[result.cigar.beg_ref : result.end_ref + 1]

    print(result.score)
    print(s_sub)
    print(t_sub)


if __name__ == "__main__":
    main()
