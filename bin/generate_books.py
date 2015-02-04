

import os, shutil


books = [
    'tactic-end-user'
]

    # 'tactic-developer',
    # 'tactic-end-user',
    # 'tactic-quickstart',
    # 'tactic-setup',
    # 'tactic-sys-admin'

media_books = [
    'tactic-developer',
    'tactic-end-user',
    'tactic-setup',
    'tactic-quickstart',
    'tactic-sys-admin'
]

plugin_books = [
    'adobe-photoshop',
    'cg-toolset',
    'foundry-nuke',
    'iridas-framecycler'
]

def copy_media(dir):
    for root, dirs, files in os.walk(dir):
        if 'media' in dirs:
            path = '%s/media'%(root)
            images = os.listdir(path)
            for image in images:
                image_path = '%s/%s' %(path, image)
                if not os.path.exists( "../build/media/"):
                    os.makedirs( "../build/media/")
                shutil.copy(image_path, "../build/media/")

for book in media_books:
    dir = '../section/doc/%s'%book
    copy_media(dir)

for book in plugin_books:
    dir = '../section/plugin/%s'%book
    copy_media(dir)
    
    

for book in books:
    cmd = 'asciidoc -b docbook ../book/%s.adoc' % book
    print
    print cmd
    print
    os.system(cmd)

    xml_path = "../build/%s.xml" % book
    if os.path.exists(xml_path):
        os.unlink(xml_path)
    shutil.move("../book/%s.xml" % book, xml_path)

    #cmd = 'xsltproc --nonet /etc/asciidoc/docbook-xsl/chunked.xsl %s.xml' % book
    

    cmd = 'a2x -D ../build -f chunked  %s' % xml_path
    print
    print cmd
    print
    os.system(cmd)

    cmd = 'a2x -D ../build -f xhtml %s' % xml_path
    print
    print cmd
    print
    os.system(cmd)

    cmd = 'a2x -D ../build -f pdf %s' % xml_path
    print
    print cmd
    print
    os.system(cmd)
    
    os.unlink(xml_path)




