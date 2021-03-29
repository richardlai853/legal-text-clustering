import csv

with open('lei.txt') as f:
    lines = f.readlines()

cnt = 0

current_dept = ''
current_lei = ''
current_chapter = ''
current_chapter_title = ''
first_line_of_chapter = False
current_article = ''
current_article_title = ''
first_line_of_article = False

output = []

for line in lines:
    if first_line_of_chapter:
        # print(line.replace('\n', ''))
        current_chapter_title = line.strip('\n')
        first_line_of_chapter = False
        continue  # because this is the first line, skip to next line to process
    if first_line_of_article:
        # print(line.replace('\n', ''))
        current_article_title = line.strip('\n')
        first_line_of_article = False
        continue

    if line.startswith('DEPT'):
        cnt = cnt + 1
        current_dept = line.split('-')[1].replace('\n', '')  # get current dept name from tags
        # print('dept', current_dept.replace('\n', ''))
    elif line.startswith('第') and line.endswith('法規\n'):
        current_lei = line[line.index('第') + 1:line.index('號')]  # get current lei number
        # print('lei', current_lei)
    elif line.startswith('第') and line.endswith('法令\n'):
        current_lei = line[line.index('第') + 1:line.index('號')]  # get current lei number
        # print('lei', current_lei)
    elif line.startswith('第') and line.endswith('章\n'):
        first_line_of_chapter = True  # mark the next line as the first line of this chapter, normally the title
        current_chapter = line.replace('\n', '')
        # print(line.replace('\n', ''))
    elif line.startswith('第') and line.endswith('條\n'):
        first_line_of_article = True  # mark the next line as the first line of this chapter, normally the title
        current_article = line.replace('\n', '')
        # print(line.replace('\n', ''))
    else:
        if first_line_of_article is False and first_line_of_chapter is False:
            payload = {'dept': current_dept, 'lei': current_lei, 'chapter': current_chapter,
                       'chapter_title': current_chapter_title,
                       'article': current_article, 'article_title': current_article_title, 'content': line.strip('\n')}
            output.append(payload)
            # print(current_dept, current_lei, current_chapter, current_article, line)

with open('lei_ouput.csv', mode='w') as lei_file:
    lei_writer = csv.writer(lei_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for item in output:
        lei_writer.writerow(
            [item['dept'], item['lei'], item['chapter'], item['chapter_title'], item['article'], item['article_title'],
             item['content']])
