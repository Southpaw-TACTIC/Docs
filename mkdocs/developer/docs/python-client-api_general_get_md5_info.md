# get\_md5\_info

**get\_md5\_info(md5\_list, texture\_codes, new\_paths, parent\_code, texture\_cls, file\_group\_dict, project\_code)**

Get md5 info for a given list of texture paths, mainly returning if this md5 is a match or not
**param:**

**md5\_list** - md5\_list

**new\_paths** - list of file\_paths

**parent\_code** - parent code

**texture\_cls** - Texture or ShotTexture

**file\_group\_dict** - file group dictionary storing all the file groups

**project\_code** - project\_code

**mode** - texture matching mode (md5, file\_name)

**return:**

**dictionary** - a dictionary of path and a subdictionary of is\_match, repo\_file\_code, repo\_path, repo\_file\_range
