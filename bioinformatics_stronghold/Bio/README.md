# A toy bioinformatics package


## Examples 

### Find the reverse complement of all the sequences in a file:

```{python}
with open('out.fasta', 'w') as f:
  for seq in Bio.read_fasta('in.fasta'):
    f.writelines(seq.reverse_complement().to_fasta())
```

### Count the number of occurrences of 'ATG' in seq1

```{python}
seq1.count('ATG')
```

### Count the number of occurrences of 'ATG' in seq1 that differ by <= 1 base.

```{python}
seq1.count('ATG', 1)
```

### ASCI plot the relative nt counts for all the sequences in a file
```{python}
for seq in Bio.read_fasta('in.fasta'):
  counts = seq.counts
  print(f">{seq.id}")
  for nt in sorted(counts.keys()):
    bar = int((counts[nt]/len(seq))*100)
    print(f"{nt}: {'◊' * bar}")

>HSBGPG Human gene for bone gla protein (BGP)
A: ◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊
C: ◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊
G: ◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊
T: ◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊
>HSGLTH1 Human theta 1-globin gene
A: ◊◊◊◊◊◊◊◊◊◊◊◊◊◊
C: ◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊
G: ◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊
T: ◊◊◊◊◊◊◊◊◊◊◊◊◊◊◊
```
