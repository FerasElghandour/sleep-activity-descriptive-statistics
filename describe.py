"""Descriptive statistics with explicit finite-data and variance conventions."""
import argparse
import csv
import json
import math
import statistics
from pathlib import Path

def quantile(values,p):
    if not values or not 0 <= p <= 1:raise ValueError('Nonempty values and p in [0,1] required')
    values=sorted(values);position=(len(values)-1)*p;lo=math.floor(position);hi=math.ceil(position)
    return values[lo]+(values[hi]-values[lo])*(position-lo)

def describe(values):
    values=[float(x) for x in values]
    if len(values)<2 or not all(math.isfinite(x) for x in values):
        raise ValueError('At least two finite numeric observations required')
    q1,q3=quantile(values,.25),quantile(values,.75);iqr=q3-q1
    lower,upper=q1-1.5*iqr,q3+1.5*iqr
    return {'n':len(values),'mean':statistics.mean(values),'median':statistics.median(values),
            'modes':sorted(statistics.multimode(values)), 'sample_sd':statistics.stdev(values),
            'population_sd':statistics.pstdev(values),'min':min(values),'max':max(values),
            'q1':q1,'q3':q3,'iqr':iqr,'outlier_fences':[lower,upper],
            'outlier_count':sum(x<lower or x>upper for x in values)}

def analyze_csv(path,columns):
    with Path(path).open(newline='') as f:rows=list(csv.DictReader(f))
    if not rows:raise ValueError('CSV is empty')
    missing=set(columns)-rows[0].keys()
    if missing:raise ValueError(f'Missing columns: {sorted(missing)}')
    return {column:describe([row[column] for row in rows]) for column in columns}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('csv',type=Path);parser.add_argument('--columns',nargs='+',default=['Physical Activity Level','Daily Steps','Heart Rate'])
    args=parser.parse_args();print(json.dumps(analyze_csv(args.csv,args.columns),indent=2))
