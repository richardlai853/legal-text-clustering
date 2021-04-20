import jieba


def seg_with_jieba(infile, outfile):
    '''segment the input file with jieba'''
    with open(infile, 'r', encoding='utf-8') as fin, open(outfile, 'w', encoding='utf-8') as fout:
        i = 0
        for line in fin:
            seg_list = jieba.cut(line)
            seg_res = ' '.join(seg_list)
            fout.write(seg_res)
            i += 1
            if i % 1000 ==0:
                print('handing with {} line'.format(i))


infile = 'zhwiki_t.txt'
outfile = 'zhwiki_t_seg.txt'

seg_with_jieba(infile=infile,outfile=outfile)
