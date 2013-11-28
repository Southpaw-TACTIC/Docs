

import os, shutil


books = [
    'tactic-developer',
    'tactic-end-user',
    'tactic-setup'
]


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
    cmd = 'a2x -D ../build -f chunked %s' % xml_path
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





