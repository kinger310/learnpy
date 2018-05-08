# https://www.sec.gov/Archives/edgar/data/1691445/000156459018009574/0001564590-18-009574-index.htm

# import pdfkit
#
# pdfkit.from_url('https://www.sec.gov/Archives/edgar/data/1691445/000156459018009574/ppdf-20f_20171231.htm',
#                 'ppdf_2017.pdf')
import os
import sys
print(sys.argv)
BAC = sys.argv[1] if len(sys.argv) > 1 else 0
print(BAC)

pythonpath = os.path.split(os.path.realpath(__file__)) #os.path.split(os.path.realpath(__file__))[0]
print(pythonpath)

if __name__ == '__main__':
    import sys

    print(BAC)
