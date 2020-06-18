# http-hooks

This is intended to be used to listen to http hooks, and wire them into shell commands.
Requests are validated against a supplied hash of the request body, which is expected to contain the time of the request.
Valid requests are then echoed onto a different port, which can be listened for behind a firewall on the server host.

Crudely, I'm greping netcat output to match urls on this inner port.  It works.
