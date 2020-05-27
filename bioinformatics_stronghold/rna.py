SAMPLE_DATASET = """GATGGAACTTGACTACGTAAATT"""
SAMPLE_OUTPUT = """GAUGGAACUUGACUACGUAAAUU"""

def solution(dataset):
    string = dataset[0].strip()
    return string.replace('T', 'U')