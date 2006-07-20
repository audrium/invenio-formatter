# -*- coding: utf-8 -*-
## $Id$

## This file is part of CDS Invenio.
## Copyright (C) 2002, 2003, 2004, 2005 CERN.
##
## The CDSware is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## The CDSware is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with CDSware; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

def format(bfo, place_label, publisher_label, date_label, separator=', ',):
    """
    Print imprint (Order: Name of publisher, place of publication and date of publication).

    @param separator a separator between the elements of imprint
    @param place_label a label to print before the publication place value
    @param publisher_label a label to print before the publisher name
    @param date_label a a label to print before the publication date
    @see place.py, publisher.py, date.py, reprints.py
    """
    
    place = bfo.field('260$a')
    publisher = bfo.field('260$b')
    date = bfo.field('260$c')
    
    out = ""
    

    if publisher != "sine nomine":
        out += publisher_label, publisher,

    if place != "sine loco":
        out+= place_label, place,

    if len(date) > 0:
        out+= date_label, date,



