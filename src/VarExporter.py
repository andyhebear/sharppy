# This is derived from the Pyste version of VarExporter.py.
# See http://www.boost.org/ for more information.

from Exporter import Exporter
from settings import *
import utils

#==============================================================================
# VarExporter
#==============================================================================
class VarExporter(Exporter):
    '''Exports a global variable.
    '''

    def __init__(self, info):
        Exporter.__init__(self, info)


    def Export(self, codeunit, exported_names):
        if self.info.exclude: return
        decl = self.GetDeclaration(self.info.name)
        if not decl.type.const: 
            msg = '---> Warning: The global variable "%s" is non-const:\n' \
                  '              changes in Python will not reflect in C++.'
            print msg % self.info.name
            print
        rename = self.info.rename or self.info.name
        code = self.INDENT + namespaces.python
        code += 'scope().attr("%s") = %s;\n' % (rename, self.info.name)
        codeunit.Write('module', code)


    def Order(self):
        return 0, self.info.name


    def Name(self):
        return self.info.name
