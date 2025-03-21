# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstateProperty(models.Model):
  _name = 'estate.property'
  _description = 'Real Estate Management'

  name = fields.Char(string='Property Name', required=True)
  description = fields.Text(string='Description')
  price = fields.Float(string='Price')
  location = fields.Char(string='Location')
  property_type = fields.Selection([
      ('house', 'House'),
      ('apartment', 'Apartment'),
      ('land', 'Land'),
  ], string='Property Type', default='house')
  status = fields.Selection([
      ('available', 'Available'),
      ('sold', 'Sold'),
  ], string='Property Status', default='available')


  # A method to fetch properties that are currently available
  def get_available_properties(self):
      return self.env['estate.property'].search([('status', '=', 'available')])

  # A method to fetch properties that are sold
  def get_sold_properties(self):
      return self.env['estate.property'].search([('status', '=', 'sold')])

  # A method to change the status of a property (e.g., mark as sold)
  def change_property_status(self, new_status):
      if new_status in ['available', 'sold']:
          self.write({'status': new_status})
