import opencc
import logging

logger = logging.getLogger()

zhwiki_raw = 'zhwiki_raw.txt'
file_output = 'zhwiki_t.txt'

with open(zhwiki_raw, 'r') as f_in, open(file_output, 'w') as f_out:
    num_total = 0
    converter = opencc.OpenCC('s2t.json')
    for num, line in enumerate(f_in):
        f_out.writelines([
            converter.convert(line)])
        num_total = num + 1
        if num_total % 10000 == 0:
            logger.info('Converted %s lines' % num_total)
    logger.info('Finished, Converted %s lines' % num_total)
