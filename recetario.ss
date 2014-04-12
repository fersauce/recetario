[epydoc] # Epydoc section marker (required by ConfigParser)

# Information about the project.
name: recetario
url: http://localhost:8000/ss

# The list of modules to document.  Modules can be named using
# dotted names, module filenames, or package directory names.
# This option may be repeated.


modules: recetario, principal

# Write html output to the directory "apidocs"
output: pdf
target: recetario/static/ssdocs
