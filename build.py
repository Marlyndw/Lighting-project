from jinja2 import Template
import glob
import os

all_html_files = glob.glob('content/*.html')
#print(all_html_files)
output = glob.glob("docs'*.html'")
base = open("template/base.html").read()
pages = []


#Phase 1
def auto_generate():

   for page in all_html_files:
        page_content = os.path.basename(page)
        name_only, entension = os.path.splitext(page_content)
        
        pages.append({
        'file_name': page,
        'output': page_content,
        'title': name_only,
        })
#        print('meow', pages)



def process_page():
    #print(pages)
    for page in pages:
        page_content = open(page['file_name']).read()
        title = page["title"]
        file_name = page["file_name"]
        template = Template(base)
        final_page = template.render(title=title, content=page_content, pages=pages)
        output_filename = 'docs/' + page["output"]
        open(output_filename, "w+").write(final_page)

    '''
    Fully process a single page dictionary
    '''
def main():


    for page in pages:
        #print('Processing', page['title'])
        process_page()
    print('Done!')

if __name__ == '__main__':
    auto_generate()
    main()
    #process_page(pages)    
#Phase 2


#Phase 3


