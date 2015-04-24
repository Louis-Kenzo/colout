
def theme():
    neutral="white"
    informative="cyan"     # e.g. 117
    choice="magenta"       # e.g. 135
    error="red"            # e.g. 197
    warning="blue"         # e.g. 214
    section_label="blue"   # e.g. 214
    section_title="green"  # e.g. 154
    second_class_object="yellow" # e.g. 230
    first_class_object="green" # e.g. 154

    return [
        # qibuild configure
        [ "^(Current build worktree:) (.*/)([^/]+)$", ",".join([section_label,section_title,section_title]), "normal,normal,bold" ],
        [ "^(Using (?:toolchain|profile):) (.*)$", ",".join([section_label,section_title]), "normal,bold" ],
        [ "^(Build type:) (.*)$", ",".join([section_label,section_title]), "normal,bold" ],
        [ "^(\* \( *[0-9]+/[0-9]+\)) (Configuring) (.*)", ",".join(["red", section_label,section_title]), "bold,bold,bold" ],
        # qibuild warning
        [ "^(\[WARN \]:) (.*)", error, "normal,bold" ],
        [ "^-- Library: (.*)$", second_class_object, "bold" ],
        [ "^-- Binary: (.*)$", first_class_object, "bold" ],
        # CMake configure
        [ "^-- (The) (.* compiler) (identification is) (.*)$", ",".join([neutral,neutral,neutral,informative]), "normal,bold,normal,bold" ],
        [ "^-- (Check for working) ([^ ]+ compiler): (.*/)([^/]+)( -- works)$", ",".join([neutral,neutral,neutral,informative]), "normal,bold,normal,bold" ],
        [ "^-- (Detecting) ([^ ]+ compiler ABI info - done)$", neutral, "normal,bold" ],
        [ "^-- (Looking for include files?) ([^ ]+) (- found)$", ",".join([neutral,informative,informative]), "normal,bold,bold" ],
        [ "^-- (Looking for include files?) ([^ ]+) (- not found)$", error, "normal,bold" ],
        [ "^-- (Looking for) ([^ ]+) (in) (.*) (- found)$", ",".join([neutral,informative,neutral,neutral,informative]), "normal,bold,normal,normal,bold" ],
        [ "^-- (Looking for) ([^ ]+) (in) (.*) (- not found)$", error, "normal,bold,normal,normal,bold" ],
        [ "^-- (Looking for) ([^ ]+) (- found)$", ",".join([neutral,neutral,neutral]), "normal,bold,bold" ],
        [ "^-- (Looking for) ([^ ]+) (- not found)$", error, "normal,bold" ],
        [ "^-- (Configuring done)$", informative, "bold" ],
        [ "^-- (Generating done)$", informative, "bold" ],
        [ "^-- (Build files have been written to:) (.*/)([^/]+)$", choice, "bold,normal,bold" ],
        [ "^-- (Using) (.*)$", choice, "normal,bold" ],
        [ "^-- (No) (.*) (library found,) (.*) (won't be built.)$", error, "normal,bold,normal,bold,normal" ],
        [ "^-- (Build Options:)$", choice, "bold" ],
        [ "^-- (WITH_.* : .*)$", choice, "bold" ],
        [ "^-- (Found) (.*): (.*) (\(found version) (.*)(\))$", informative, "normal,bold,bold,normal,bold,normal" ],
        # CMake build
        [ "^(\* \( *[0-9]+/[0-9]+\)) (Building) (.*)", ",".join(["red", section_label,section_title]), "bold,normal,bold" ],
        [ "^(Scanning dependencies of target) (.*)$", neutral, "normal,bold" ],
        [ "^\[\s*[0-9]+%\]\s(Building \w* object)(\s+.*/)([-\w]+.c.*)(.o)$", informative, "normal,normal,bold,bold"],
        [ "^\[\s*[0-9]+%\]\s(Built target)(\s.*)$", ",".join([section_label,section_title]), "normal,bold" ],
        [ "^(Linking .*) (shared library|library|executable) (.*/)*(.+(\.[aso]+)*)$", neutral, "normal,normal,normal,bold,bold" ],
        [ "^\[\s*[0-9]+%\]\s(Generating)(\s+.*)$", neutral, "normal" ],
        # CMake errors and warnings
        [ "^-- Found.*NO", error ],
        [ "^--.*broken", error ],
        [ "^-- Coult NOT find.*", error ],
        [ "^-- Configuring incomplete, errors occurred!", error ],
        [ "CMake Error:", error, "reverse" ],
        [ "CMake Warning", warning, "reverse" ],
        # make errors
        [ "make\[[0-9]+\].*", "yellow"],
        [ "(make: \*\*\* \[.+\] )(.* [0-9]+)", error, "normal,bold"],
        # Progress percentage
        [ "^(\[\s*[0-9]+%\])","Scale" ]
    ]
