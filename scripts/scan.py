# -*- coding: latin1 -*-

# This file is part of AFPT.

# AFPT is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# AFPT is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with AFPT.  If not, see <http://www.gnu.org/licenses/>
# You can read the license.txt in parent directory

import os
import sys


def scan(adress):
    path = os.path.abspath('.')
    list_test = []
    for root, dirs, files in os.walk(adress):  # Parcours le disque
        for file in files:
            if file:
                try:
                    log = open(path + '/tmp/log_tree.txt', 'a')
                    list_test.append(os.path.join(root, file))
                    sys.stdout.write("\rNombre de fichiers trouvés: {0}".format(len(list_test)))
                    log.write(os.path.join(root, file))
                    log.write("\n")
                    log.close()
                    lien = os.path.join(root, file)
                except:
                    pass





    


