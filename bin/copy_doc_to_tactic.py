import shutil
import os

class CopyDoc(object):

    def __init__(my):
        my.src_base_dir = '/home/tactic/Docs/build'
        my.dest_base_dir = '/home/tactic/tactic/doc/book/doc'
        my.book_types = ['developer','end-user','quickstart','setup','sys-admin']
        
    def clean_up(my):
        
        for book_type in my.book_types:
            book_dir = '%s/doc_tactic-%s'%(my.dest_base_dir, book_type)
            if os.path.exists(book_dir):
                shutil.rmtree(book_dir)
            os.makedirs(book_dir)


    def copy(my):

        for book_type in my.book_types:
            dest_book_dir = '%s/doc_tactic-%s'%(my.dest_base_dir, book_type)
            dest_html_dir = '%s/html' %(dest_book_dir)
            src_dir = '%s/tactic-%s.chunked' %(my.src_base_dir, book_type)
            shutil.copytree(src_dir, dest_html_dir)
            pdf_path = '%s/tactic-%s.pdf'%(my.src_base_dir, book_type)
            shutil.copy(pdf_path, dest_book_dir)

        
    def execute(my):
        my.clean_up()
        my.copy()



if __name__ == '__main__':
    
    command = CopyDoc()
    command.execute()

