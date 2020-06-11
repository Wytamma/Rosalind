from .seq import Seq


def test_init():
    assert type(Seq("TATA")) == Seq


def test_repr():
    seq1 = Seq("TATA")
    seq2 = Seq("TATA", id="seq2")
    assert repr(seq1) == "Seq(TATA)"
    assert repr(seq2) == "Seq(TATA, id='seq2')"


def test_str():
    seq = Seq("TATA")
    assert str(seq) == "TATA"


def test_len():
    seq = Seq("TATA")
    assert len(seq) == 4


def test_invert():
    seq = Seq("GGAATT")
    assert (~seq).sequence == "AATTCC"


def test_add():
    seq1 = Seq("GGAATT")
    seq2 = Seq("TATA")
    assert (seq1 + seq2).sequence == "GGAATTTATA"

def test_sub():
    seq1 = Seq("TTTT")
    seq2 = Seq("TATA")
    assert (seq1 - seq2) == 2

def test_gc():
    seq = Seq("GCAT")
    assert seq.gc == 50


def test_counts():
    seq = Seq("GGAATT")
    assert seq.counts == {"G": 2, "A": 2, "T": 2}


def test_fasta():
    seq = Seq(
        id="Example fasta",
        sequence="GGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATT",
    )
    fasta = (
        ">Example fasta\n"
        "GGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGG\n"
        "AATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAA\n"
        "TTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATTGGAATT\n"
        "GGAATT"
    )
    assert seq.to_fasta() == fasta
