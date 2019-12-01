# add\_group

**add\_group(snapshot\_code, file\_path, file\_type, file\_range, use\_handoff\_dir=False, mode=None)**

Add a file range to an already existing snapshot

**param:**

**snapshot\_code** - the unique code identifier of a snapshot

**file\_path** - path of the file to add to the snapshot

**file\_type** - type of the file to be added.

**file\_range** - range with format s-e/b

**keyparam:**

**use\_handoff\_dir** - use handoff dir to checkin file

**mode** - one of 'copy','move','preallocate'

**return:**

**dictionary** - the resulting snapshot
