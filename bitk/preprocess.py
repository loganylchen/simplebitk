# AUTOGENERATED! DO NOT EDIT! File to edit: 06_preprocess.ipynb (unless otherwise specified).

__all__ = ['featurecount_rename']

# Cell

import pandas as pd

# Cell

def featurecount_rename(featurecounts,clinical,prefix,*,sample_title='sample',bam_title='bam',count_title='Geneid'):
    '''
    featurecounts will use the bamfile name as the sample name. This script rename the featurecounts by the given table.

    :param str featurecounts: featurecounts table file
    :param str clinical: clinical table file with header
    :param str prefix: output prefix, there will be two outputs, one is count output (prefix_count.txt), and the other one is the rename featurecounts (prefix_fc.txt)
    :param str sample_title: the column name of the sample name
    :param str bam_title: the column name of the bamfile name
    :param str count_title: the column name used as identity in count data
    '''

    fc = pd.read_csv(featurecounts,sep='\t',comment='#')
    cli = pd.read_csv(clinical,sep='\t',comment='#')
    fc.rename(columns=cli.set_index(bam_title)[sample_title],
                 inplace=True)
    fc.to_csv(f'{prefix}_featurecounts.txt',sep='\t',index=False)
    fc[[count_title]+list(cli[sample_title])].to_csv(f'{prefix}_counts.txt',sep='\t',index=False)