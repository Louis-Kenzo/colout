
def theme():
    subdued = "black"  # e.g. 242
    neutral = "white"  # e.g. 117
    info    = "cyan"   # e.g. 117
    error   = "red"    # e.g. 197
    warning = "yellow" # e.g. 214

    numbering = "white"
    absolute_filename = "magenta"
    number = "yellow"
    ip = "green"
    time = "red"

    return [
        [ " (?:[0-9]+\.[0-9]+ )?[0-9]+ ((?:[a-zA-Z]+[.])*[a-zA-Z]+): ", "hash" ],
        [ "\] ([0-9]+\.[0-9]+ )?([0-9]+) ", subdued ],
        [ "^(\[D\]) ", subdued ],
        [ "^(\[V\]) ", neutral ],
        [ "^(\[I\]) ", info ],
        [ "^(\[W\]) ", warning, "bold" ],
        [ "^(\[E\] )", error, "reverse" ],
        [ " Registered Service \"([a-zA-Z0-9]+)\" \(#[0-9]+\)", neutral, "bold" ],
        [ "#[0-9]+", numbering ],
        [ "(/(?:[^/]+/)+)([^/]+\.[a-zA-Z0-9]+)", absolute_filename, "normal,bold" ],
        [ "^(tail\:) \S+\: (file truncated)", "white", "reverse"],
        [ "\s[0-9]+[\s$]", number],
        [ "(?:[a-z]+\://)([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)(?:\:[0-9+])", ip, "bold"],
        [ "([0-9]{4}-[0-9]{2}-[0-9]{2}) ([0-9]{2}\:[0-9]{2})(\:[0-9]{2}) ([A-Z]+(?:[+-][0-9]{1,2})?)", time, "normal,bold,normal"],
        [ "\s(starting NAOqi version \d\.\d{1,2}\.\d{1,2})\s", "cyan", "reverse"],
        [ "\s(NAOqi is ready)\.\.\.\s", "yellow", "reverse"]
    ]
