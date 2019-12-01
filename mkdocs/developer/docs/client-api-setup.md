# Client API Setup

**Important Note**

Visit the Southpaw support site for more examples and tutorials on the
API and its usage. The Support site is the place to go for wikis,
forums, examples, and more.

**Setup**

The easiest way to interact with the server from the client using the
Client API is to use the provided server stub code. This code includes a
class and a utility that are very useful for handling many of the
details around client/server interaction and authentication.

The server stub code is housed in a client folder and can be found in
the TACTIC installation in the directory:

    <tactic_install_dir>/src/client

The first step is to copy the entire client folder over to the client
machine (the machine that will be running the scripts) to a directory
that will be visible to the user. Most facilities would likely put this
folder in a centralized location so that every computer would be able to
execute its scripts. The path to this folder must be specified in the
PYTHONPATH environment variable on client machines so that it can be
found by the scripts. For instance, if PYTHONPATH = L:/custom\_python.
you would put the client folder in L:/custom\_python. Please refer to the
Python documentation for more information.

**Settings**

There are three important parameters for setting up the TacticServerStub
to connect correctly :

-   server: specifies the server that the server stub will connect to.
    This server can be a domain name ("localhost") or an IP address ("127.0.0.1"). It can even be a port number ("localhost:9000"). This
    setting allows you to switch between various TACTIC servers in your facility.

-   project: specifies the current project. In TACTIC, the project is a
    state under which interactions occur.

-   ticket: specifies the authentication ticket, a long alpha-numeric
    string that encrypts the login and password so that these values remain secure.

There are a number of methods to set these parameters.

The **first method** is to set the following parameters directly in the
server stub reference:

    server = TacticServerStub()
    server.set_server(tactic_server)
    server.set_project(project)
    # this is not needed if you have run python get_ticket.py
    server.set_ticket(ticket)

These settings override all settings obtained elsewhere. This method
ensures that these values are set up correctly based on some external
information.

To set up a server stub, you can insert the stub information in your
script (described in the client API documentation as part of the
get\_ticket() function). Or, you can run the script **get\_ticket.py**,
which is included with the client API example set (located in
&lt;TACTIC\_INSTALL\_DIR&gt;/src/client/bin). When the stub is run, it creates a
ticket file on the user’s machine which will be used each time any API
script is run to authenticate which user is running the script.

The **second method** is through environment variables set up across the
studio:

-   TACTIC\_SERVER: sets the server that the server stub will connect to.

-   TACTIC\_PROJECT: sets the project that the server stub will connect to.

-   TACTIC\_TICKET: sets the authentication ticket.

This method can be used by programs that set up user environments, and
has other advantages. It is easy to switch the settings using a shell
variable. The program that sets up the environment does not have to be
written in Python. It can even be simple to set up by using a shell
command line to set the environment variables.

The **third method** makes use of a resource file located in the user’s
home directory. This resource file has a simple format:

    login=joe
    server=localhost
    ticket=97d2bec3d73da71c14fb724a47af5053
    project=bar

The login tag doesn’t actually do anything here, since the user name is
encapsulated in the ticket itself.

The **fourth method** is described below:

If you have written a GUI or have some means of retrieving the user’s
password on individual session instead, you can use the following
construct to set the ticket. The server’s IP and project should be set
beforehand.

         server = TacticServerStub.get()
         server_IP = '10.10.50.100'
         my.set_server(server_IP)
         my.set_project('sample3d')

         ticket = my.get_ticket(login, password)
         my.set_ticket(ticket)

Once you have set up the environment for the client API to run
correctly, you can try a sample script. The following simple script
illustrates the structure of a TACTIC Client API program:

    import sys
    from tactic_client_lib import TacticServerStub

    def main(args):
        server = TacticServerStub()
        server.start("Ping Test")
        try:
            print server.ping()
        except:
            server.abort()
            raise
        else:
            server.finish()

    if __name__ == '__main__':
        executable = sys.argv[0]
        args = sys.argv[1:]
        main(args)

This simple program will ping the server and return "OK". If everything
is set up correctly, you should be able to run this program from a shell
as follows:

    # python ping.py
    OK

If you see "OK", then you have successfully connected to the TACTIC
server using the client API.

If you need to run python get\_ticket.py first, it can be found under:
client/bin/get\_ticket.py.
