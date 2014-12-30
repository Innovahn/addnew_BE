# -*- encoding: utf-8 -*-

#import itertools
#from lxml import etree

from openerp.osv import osv, fields
#from openerp import models, fields, api, _
#from openerp.exceptions import except_orm, Warning, RedirectWarning
#import openerp.addons.decimal_precision as dp
#import openerp
#from openerp.tools.float_utils import float_round as round
import openerp.addons.decimal_precision as dp

class invoice_discount(osv.Model):
	_inherit = 'account.invoice.line'
	decription = 'Invoice whit discount different'

	#funcion que calcula y guarda en la bd el valor del subtotal al hacer click en guardar
	def _calcula_precio(self, cr, uid, ids,name,args=None,context=None):
		result={}
		for invoice in self.browse(cr,uid,ids,context=context):
			total=invoice.quantity * invoice.price_unit
			total_desc=total-(invoice.quantity * invoice.discount_amount)			
			self.write(cr,uid,invoice.id,{'p_subtotal':total_desc},context=context)
			result[invoice.id]=total_desc
		return result

	#funcion que calcula y muestra el valor del subtotal en la vista
	def _calcula_precio_onchange(self, cr, uid, ids,quantity,discount_amount,price_unit,context=None):
		total=quantity * price_unit
		return {'value' : {'p_subtotal' : total-(quantity * discount_amount) or 17.0}}
	
	
	_columns ={
	#'monto_total' : fields.function(_calcula_total,type='float'),    
	'discount_amount' : fields.float('Discount', default=0.0),
	'p_subtotal' : fields.function(_calcula_precio,type='float',store={'account.invoice.line':(_calcula_precio,['discount_amount','price_unit','quantity'],0)}),	
	#'p_subtotal' : fields.function(_calcula_precio,'Amount S',type='float',default=0.0,store=True,readonly=True,digits= dp.get_precision('Account')),
	}
class invoice_total(osv.Model):
	_inherit = 'account.invoice'
	decription = 'Amount total whithout tax'

	def _calcula_total(self, cr, uid, ids,field,arg,context=None):
		result={}
		print "-"*50
		print ids
		for invoice in self.browse(cr,uid,ids,context=context):
			invoice.amount_untaxed = sum(line.p_subtotal for line in invoice.invoice_line)
		        invoice.amount_tax = sum(line.amount for line in invoice.tax_line)
	        	monto_total = invoice.amount_untaxed + invoice.amount_tax
		#	invoice.amount_total=monto_total
			self.write(cr,uid,invoice.id,{'amount_total':monto_total},context=context)
		#	result[invoice.id]=monto_total
		#return result

	#_columns={
	#'monto_total':fields.function(_calcula_total,type='float'),	
	#}



	
	
	

	
