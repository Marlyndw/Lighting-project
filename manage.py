from jinja2 import Template
import glob
import os

all_html_files = glob.glob('content/*.html')
#print(all_html_files)
output = glob.glob("docs'*.html'")
base = open("template/base.html").read()
pages = []

def main():


    for page in pages:
        #print('Processing', page['title'])
        process_page()
    print('Done!')

if __name__ == '__main__':
    auto_generate()
    main()

