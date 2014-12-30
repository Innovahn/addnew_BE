# -*- encoding: utf-8 -*-

import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp
from openerp.tools.translate import _

class account_assets(osv.osv):
    _inherit = 'account.asset.asset'
    decription = 'Asset with new fields'

    _columns ={
    		'ubication':fields.char('Asset Ubication',help="The ubication of this assets"),    
		'assigned_to':fields.char('Assigned to',help="The asset is assigned"),
		'date_assigned':fields.date('Date asigned',help="This is the date when was assigned an asset"),
		'returned':fields.boolean('Returned Asset',help="This is checked when tha asset was returned"),
	}
