# Advanced Schema Configuration

**Advanced Schema Configuration**

When creating a search type, the "Search Type" property defines the
project schema (project\_namespace) and name for the search type. For
example, if your current project is called **media** then adding a new
search type named "artwork" into the interface will automatically
generate "media/artwork" and it will be added to the media project’s
schema

**Schema XML Structure**

    <?xml version='1.0' encoding='UTF-8'?>
    <schema>
      <search_type name='media/training_videos'/>
      <search_type name='media/script'/>
      <connect to='media/script' type='hierarchy' from='media/training_videos'/>
      <search_type name='media/fonts'/>

    </schema>

To add a new search for a different schema, all that is required is an
explicit definition of the full Search Type
"&lt;project\_namespace&gt;/&lt;name&gt;".

For example to add an "artwork" search type in the "media" namespace,
you would define the search type as "media/artwork". The specific schema
information will be added to your current project only.
