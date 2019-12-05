# add\_directory

**add\_directory(snapshot\_code, dir, file\_type='main', mode="copy", dir\_naming='', file\_naming='')**

Add a full directory to an already existing checkin.
This informs TACTIC to treat the entire directory as single entity
without regard to the structure of the contents. TACTIC will not
know about the individual files and the directory hierarchy within
the base directory and it it left up to the and external program
to intepret and understand this.

This is often used when logic on the exact file structure exists in
some external source outside of TACTIC and it is deemed to complictaed
to map this into TACTIC’s snapshot definition.

**param:**

**snapshot\_code** - a unique identifier key representing an sobject

**dir** - the directory that needs to be checked in

**keyparam:**

**file\_type** - file type is used more as snapshot type here

**mode** - copy, move, preallocate, manual, inplace

**dir\_naming** - explicitly set a dir\_naming expression to use

**file\_naming** - explicitly set a file\_naming expression to use

**return:**

**dictionary** - snapshot

**example:**

This will create a new snapshot for a search\_key and add a directory using manual mode

            dir = 'C:/images'

            handoff_dir = my.server.get_handoff_dir()

            shutil.copytree('%s/subfolder' %dir, '%s/images/subfolder' %handoff_dir)



            snapshot_dict = my.server.create_snapshot(search_key, context='render')

            snapshot_code = snapshot_dict.get('code')

            my.server.add_directory(snapshot_code, dir, file_type='dir', mode='manual')
