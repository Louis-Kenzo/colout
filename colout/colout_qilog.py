
def theme():
    subdued = "black" # e.g. 242
    neutral = "white" # e.g. 117
    info    = "white" # e.g. 117
    error   = "red"   # e.g. 197
    warning = "blue"  # e.g. 214

    return [
        [ "^(\[D\]) ", subdued, "bold" ],
        [ "^(\[V\]) ", neutral, "bold" ],
        [ "^(\[I\]) ", info, "bold" ],
        [ "^(\[W\]) ", warning, "bold" ],
        [ "^(\[E\]) ", error, "bold" ],
        [ " (?:[0-9]+\.[0-9]+ )?[0-9]+ ((?:[a-zA-Z]+[.])*[a-zA-Z]+): ", "Hash", "bold" ],
        [ " ([0-9]+\.[0-9]+ )?([0-9]+) ", subdued ],
        [ " (Registered Service) \"([a-zA-Z0-9]+)\" \(#[0-9]+\)", neutral, "underline,bold" ]
    ]
