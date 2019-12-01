# insert

**insert(search\_type, data, metadata={}, parent\_key=None, info={}, use\_id=False, triggers=True)**

General insert for creating a new sobject

**param:**

**search\_type** - the search\_type attribute of the sType

**data** - a dictionary of name/value pairs which will be used to update

the sobject defined by the search\_key.

**parent\_key** - set the parent key for this sobject

**keyparam:**

**metadata** - a dictionary of values that will be stored in the metadata attribute

if available

**info** - a dictionary of info to pass to the ApiClientCmd

**use\_id** - use id in the returned search key

**triggers** - boolean to fire trigger on insert

**return:**

**dictionary** - represent the sobject with it’s current data

**example:**

insert a new asset

            search_type = "prod/asset"



        data = {

                'code': chr001,

                'description': 'Main Character'

            }



        server.insert( search_type, data )

insert a new note with a shot parent

            # get shot key

            shot_key = server.build_search_key(search_type='prod/shot',code='XG001')



            data = {

                'context': 'model',

                'note': 'This is a modelling note',

                'login': server.get_login()

            }



            server.insert( search_type, data, parent_key=shot_key)

insert a note without firing triggers

            search_type = "sthpw/note"



            data = {

                'process': 'roto',

                'context': 'roto',

                'note': 'The keys look good.',

                'project_code': 'art'

            }



            server.insert( search_type, data, triggers=False )
