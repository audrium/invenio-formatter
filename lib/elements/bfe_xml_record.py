# -*- coding: utf-8 -*-
##
## $Id$
##
## This file is part of CDS Invenio.
## Copyright (C) 2002, 2003, 2004, 2005, 2006 CERN.
##
## CDS Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## CDS Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.  
##
## You should have received a copy of the GNU General Public License
## along with CDS Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
"""BibFormat element - Prints record as XML
"""
__revision__ = "$Id$"

def format(bfo, type='xml', encodeForXML='yes'):
    """
    Prints the complete current record as XML.

    @param type the type of xml. Can be 'xml', 'oai_dc', 'marcxml', 'xd'
    @param encodeForXML if 'yes', replace all < > and & with html corresponding escaped characters.
    """
    from invenio.bibformat_utils import record_get_xml, encode_for_xml
    #This element is mainly a bridge between BibRecord XML formatting capabilities and
    #BibFormat templates.
    
    #Can be used to output various xml flavours.
    
    out = record_get_xml(bfo.recID, format=type)

    if encodeForXML.lower() == 'yes':
        return encode_for_xml(out)
    else:
        return out
 
