# -*- coding: utf-8 -*-
##############################################################################
#
#    Law Follow Up
#    Copyright (C) 2014 Sistemas ADHOC
#    No email
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


import re
from openerp import netsvc
from openerp.osv import osv, fields

class enclosure_treatment_detail(osv.osv):
    """"""
    
    _name = 'law_tracking.enclosure_treatment_detail'
    _description = 'enclosure_treatment_detail'

    _columns = {
        'note': fields.text(string='Note'),
        'order_paper_id': fields.many2one('law_tracking.order_paper', string='Order Paper', required=True), 
        'law_project_id': fields.many2one('law_tracking.law_project', string='Law Projects', ondelete='cascade', required=True), 
    }

    _defaults = {
    }


    _constraints = [
    ]




enclosure_treatment_detail()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: