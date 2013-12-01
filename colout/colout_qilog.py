
def theme():
    return [
        [ "^\[D\] ", "white", "bold" ],
        [ "^\[V\] ", "white", "bold" ],
        [ "^\[I\] ", "117", "bold" ],
        [ "^\[W\] ", "214", "bold" ],
        [ "^\[E\] ", "197", "bold" ],
        [ "[0-9]+\.[0-9]+ [0-9]+ ([a-zA-Z]+): ", "229", "bold" ],
        [ "[0-9]+\.[0-9]+ [0-9]+ ([a-zA-Z]+[.])*([a-zA-Z]+[.])([a-zA-Z]+): ", "230,230,229", "normal,normal,bold" ],
	[ "([0-9]+\.[0-9]+) ([0-9]+) ", "242" ],
        [ " (Registered Service) \"([a-zA-Z0-9]+)\" \(#[0-9]+\)", "white", "underline,bold" ]
    ]
