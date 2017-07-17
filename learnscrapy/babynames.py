import re

def extract_babynames(filename):
    # read file
    text = open(filename, 'r').read()
    # extract names using regular expression
    info_list = []
    # pattern = r'<td>(\d+)</td><td>([A-Z]\w+)</td><td>([A-Z]\w+)</td>'
    pattern = r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>'
    tuples = re.findall(pattern, text)

    #  write your code here
    for rank, boybabyname, girlbabyname in tuples:
        info_list.append((boybabyname,'male', rank))
        info_list.append((girlbabyname, 'female', rank))
    # save results in a file
    with open(filename[:-4]+'txt','w') as fout:
        for babyname, gender, rank in sorted(info_list):
            fout.write('%s\t\t%s\t\t%s\n'%(babyname, gender, rank))

if __name__=='__main__':
    for year in range(1990, 2010, 2):
        filename = "./learnscrapy/babynames/baby%d.html" % year
        print('extracting the file %s' % filename)
        extract_babynames(filename)

